# Automated Firmware Security Assessment and Vulnerability Reporting for IoT Devices


## Overview

This project is an IoT firmware security analysis tool designed to automate the detection of common firmware vulnerabilities.

The system allows users to upload firmware files through a Flask dashboard, performs security analysis, detects risky configurations and exposed secrets, and generates vulnerability findings.



## Features

- Firmware upload through web interface
- Automated file analysis
- Hardcoded credential detection
- API key and secret token detection
- Insecure configuration detection
- Severity classification
- Risk summary dashboard
- Vulnerability report generation



## Technology Stack

- Python
- Flask
- HTML
- CSS
- SQLite (planned)
- Binwalk (planned)
- Git and GitHub



## Project Architecture


User

↓

Flask Web Interface

↓

Firmware Upload Handler

↓

Scanner Engine

↓

Security Analysis Modules

↓

Risk Analyzer

↓

Report Generation



## Modules


### Scanner Engine

Handles firmware files and performs recursive analysis.


### Secret Detector

Detects sensitive information such as:

- Password exposure
- API keys
- Secret tokens


### Configuration Analyzer

Detects insecure configurations:

- Debug mode enabled
- Telnet enabled
- Encryption disabled


### Risk Analyzer

Calculates:

- Total vulnerabilities
- High severity issues
- Medium severity issues
- Low severity issues



## Screenshots


### Firmware Dashboard

![Dashboard](screenshots/day11_risk_dashboard.png)


### Vulnerability Results

![Results](screenshots/day10_dynamic_scan.png)



## Current Status

Completed:

- Core scanner
- Security modules
- Flask integration
- Upload workflow
- Risk dashboard


Upcoming:

- Firmware extraction using Binwalk
- Database storage
- PDF report generation
- UI improvements


## Author

Smruthi Nayak
