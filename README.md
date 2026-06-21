# Nebula Shield: Automated Vulnerability Assessment for Local LLMs
<img width="732" height="891" alt="Nebula Shield 2" src="https://github.com/user-attachments/assets/8bf66347-c2c8-4289-b104-cab795f0937a" />

This repository contains the architecture, automated configuration files, and evaluation reports for the **Nebula Shield** security assessment framework. The project evaluates prompt injection vulnerabilities and data validation vectors within localized Large Language Model implementations.

## Repository Structure
* `run_scan.py`: Automated orchestration script for vulnerability scanning.
* `garak_rest.json`: REST payload structures and API connection profiles.
* `garak_configs.yaml`: Fine-tuned plugin weights and scanner thresholds.
* `nebula_shield_report.html`: Compiled vulnerability evaluation report matrix.
* `app/`: Target application middleware deployment code (synchronized from Ubuntu subsystem).
