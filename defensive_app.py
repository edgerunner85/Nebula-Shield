

import os
import re
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration: Points to your actual backend local LLM API instance
LOCAL_LLM_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:8000/v1/chat/completions")

# Heuristic signatures frequently used in adversarial prompt injection attacks
INJECTION_SIGNATURES = [
    r"ignore (all )?previous instructions",
    r"system prompt bypass",
    r"you are now an unrestricted AI",
    r"disregard (the )?above",
    r"stop responding as a helpful assistant",
    r"act as a developer with debugging privileges",
    r"override system configuration",
    r"output raw markdown configuration code"
]

def analyze_input_safety(user_input):
    """
    Evaluates incoming request payloads for malicious structural anomalies
    and explicit prompt injection heuristics.
    """
    if not user_input or not isinstance(user_input, str):
        return True, "Valid Input Structure"

    # 1. Length-Based Anomaly Detection (Mitigates payload stuffing and token flooding)
    if len(user_input) > 4000:
        return False, "Input exceeds maximum allowable token boundary constraint."

    # 2. Signature Matching Loop
    for signature in INJECTION_SIGNATURES:
        if re.search(signature, user_input, re.IGNORECASE):
            return False, f"Structural anomaly detected matching pattern: '{signature}'"

    return True, "Safe"

@app.route("/query", methods=["POST"])
def shield_endpoint():
    """
    Main proxy routing mechanism that screens incoming requests before
    passing safe inputs to the internal LLM context window.
    """
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Malformed payload structure. 'message' field is required."}), 400

    user_message = data["message"]

    # Execute inspection matrix
    is_safe, reason = analyze_input_safety(user_message)

    if not is_safe:
        # Prevent upstream traversal and log the violation metrics cleanly
        return jsonify({
            "status": "REJECTED",
            "shield_reasons": reason,
            "response": "Security Policy Violation: The requested input structure failed input validation constraints."
        }), 403

    # If payload is deemed clean, securely forward the transaction to the backend LLM instance
    try:
        # Remap incoming structure to the unified format expected by your local model
        forward_payload = {
            "model": data.get("model", "local-llm"),
            "messages": [{"role": "user", "content": user_message}],
            "temperature": data.get("temperature", 0.2)
        }
        
        response = requests.post(LOCAL_LLM_URL, json=forward_payload, timeout=10)
        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "ERROR",
            "message": "Failed to communicate with internal core processing engine."
        }), 502

if __name__ == "__main__":
    # Binds to all interfaces so your bridged Kali environment can access it over the network
    app.run(host="0.0.0.0", port=5000, debug=False)
