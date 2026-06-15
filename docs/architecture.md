# System Architecture


User

↓

Flask Dashboard

↓

Firmware Upload Handler

↓

Binwalk Firmware Extractor

↓

Scanner Engine


Scanner connects to:

- Secret Detector
- Configuration Analyzer


↓

Risk Analyzer

↓

SQLite Database

↓

Report Generator

↓

Security Dashboard