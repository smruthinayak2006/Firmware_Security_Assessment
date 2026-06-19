# Automated Firmware Security Assessment and Vulnerability Reporting for IoT Devices


## Overview

Automated IoT firmware analysis platform for detecting insecure configurations, exposed secrets, and security risks.

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
- Known vulnerability detection using CVE matching
- Firmware integrity verification using MD5 and SHA256 hashing
- Firmware risk scoring engine
- Numerical vulnerability prioritization
- SOC style security dashboard
- Risk visualization meter


## Technology Stack

- Python
- Flask
- HTML
- CSS
- SQLite Database
- Binwalk Firmware Extraction
- Git and GitHub



## Architecture

Detailed architecture documentation:

See:

docs/architecture.md


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


### CVE Checker

Detects vulnerable firmware components by comparing discovered software versions with a vulnerability database.

Detects:

- Vulnerable packages
- CVE identifiers
- Severity level


### Hash Analyzer

Calculates firmware fingerprints for integrity verification.

Generates:

- MD5 hash
- SHA256 hash

### Risk Scoring Engine

Calculates firmware security exposure using severity based scoring.

Severity weights:

- High vulnerabilities
- Medium vulnerabilities
- Low vulnerabilities


Generates:

- Firmware risk score
- Risk level classification
- Remediation priority


## Screenshots


### Flask Upload Interface

![Upload](screenshots/day8_flask_homepage.png)


### Scanner Integration

![Scanner](screenshots/day9_flask_scanner_integration.png)


### Dynamic Firmware Scan

![Dynamic Scan](screenshots/day10_dynamic_scan.png)


### Risk Analysis Dashboard

![Risk Dashboard](screenshots/day11_risk_dashboard.png)


### Final Security Dashboard UI

![Dashboard](screenshots/day15_dashboard_ui.png)


### Vulnerability Scan Results

![Results](screenshots/day15_scan_results.png)


### CVE Detection

![CVE Detection](screenshots/day17_cve_detection.png)


### Firmware Hash Integrity Analysis

![Hash Analysis](screenshots/day18_firmware_hash_integrity.png)


### Firmware Scan History

![Scan History](screenshots/day20_scan_history_dashboard.png)

### Admin Authentication

![Login](screenshots/day21_login_authentication.png)


## Current Status

Completed:

Completed:

- Core scanner
- Security modules
- Flask integration
- Upload workflow
- Risk dashboard
- Firmware metadata extraction
- Hash based integrity verification
- Scan history storage
- Authentication system
- Firmware risk scoring engine
- SOC style dashboard UI

Upcoming:

- User authentication and access control
- Dashboard security improvements
- Advanced vulnerability checks
- Deployment preparation


## Author

Smruthi Nayak
