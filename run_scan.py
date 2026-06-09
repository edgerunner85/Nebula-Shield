import sys
import garak.start

def main():
    print("[+] Launching Automated Nebula Shield Security Assessment...")
    
    # Define your structured execution variables inside clean list structures
    sys.argv = [
        "garak",
        "--model_type", "rest.RestGenerator",
        "--model_name", "Nebula Shield Lab API",
        "--probes", "promptinject",
        "--generator_options", '{"uri": "http://192.168.1.155:5000/query", "method": "post", "req_template_json_object": {"prompt": "$INPUT"}}'
    ]
    
    # Hand the variables directly into Garak's primary orchestration framework
    garak.start.main()

if __name__ == "__main__":
    main()
