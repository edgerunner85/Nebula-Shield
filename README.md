# Nebula Shield: Automated Vulnerability Assessment for Local LLMs
<img width="732" height="891" alt="Nebula Shield 2" src="https://github.com/user-attachments/assets/8bf66347-c2c8-4289-b104-cab795f0937a" />

# Nebula Shield Defensive AI Lab

Nebula Shield is a localized application security testing environment designed to demonstrate how defensive proxy middleware intercepts and mitigates adversarial prompt injections against Large Language Models.

---

## Lab Prerequisites

* **Target Host:** Ubuntu LTS with Python 3 installed.
* **Security Auditor Host:** Kali Linux with Python 3 installed.
* **Network Connectivity:** Unrestricted HTTP traffic over port 5000 between both instances.

---

## Step by Step Lab Guide

### Phase 1: Deploy the Vulnerable Target Application (Ubuntu)

1. Open a terminal on your target system and navigate into your core workspace:
   ```bash
cd ~/gem5/my_configs/nebula_shield_lab

Install the necessary lightweight web framework components to handle backend traffic routing:

Bash
pip3 install flask requests --break-system-packages

Launch your defensive application layer. This application monitors incoming payloads, acting as a structural firewall guarding the simulated model endpoints:

   '''bash
python3 defensive_app.py

Verify the system log outputs indicate the server is listening successfully on port 5000.

### Phase 2: Configure the Assessment Environment (Kali Linux)
Open your terminal console on Kali and switch to your security repository folder:

   '''bash
cd ~/Nebula-Shield

Initialize your isolated security tool suite virtual environment where the testing framework modules are stored:

   '''bash
source ~/venvs/garak/bin/activate

Configure your automated vulnerability testing suite by verifying that your REST endpoints, custom payloads, and evaluation criteria maps point directly to your active Ubuntu server IP address inside your garak_configs.yaml or garak_rest.json files.

### Phase 3: Launch automated Scanning Sweeps
Execute your custom scanning orchestration script. This script automatically targets your vulnerable application using adversarial probes to evaluate your guardrail thresholds:

   '''bash
PYTHONPATH=/home/kali/venvs/garak python3 run_scan.py

Review the resulting vulnerability metrics. The orchestration script compiles all telemetry data into an interactive visual dashboard:

   '''bash
xdg-open nebula_shield_report.html

## Repository Structure
* `run_scan.py`: Automated orchestration script for vulnerability scanning.
* `garak_rest.json`: REST payload structures and API connection profiles.
* `garak_configs.yaml`: Fine-tuned plugin weights and scanner thresholds.
* `nebula_shield_report.html`: Compiled vulnerability evaluation report matrix.
* `app/`: Target application middleware deployment code (synchronized from Ubuntu subsystem).
