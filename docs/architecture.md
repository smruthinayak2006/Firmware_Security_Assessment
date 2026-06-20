Firmware Upload
        |
        v

Firmware Analyzer
        |
        +----------------+
        |                |
        v                v

Metadata Extraction     Hash Calculation
                         (MD5 + SHA256)

        |
        v

Binwalk Extractor

        |
        v

Scanner Engine

        |
        +-------------+-------------+
        |             |             |
        v             v             v

Secret Detector   Config Analyzer   CVE Checker

        |
        v

Remediation Engine

        |
        v

Risk Analyzer
        |
        v

Risk Score Engine
        |
        v

Database Storage

        |
        v

Report Generator + Dashboard