## Current System Architecture


Firmware Upload
        |
        v
Firmware Analyzer
        |
        +----------------+
        |                |
        v                v
 Metadata Extractor   Hash Analyzer
                       (MD5/SHA256)

        |
        v

Firmware Extractor
(Binwalk)

        |
        v

Scanner Engine

        |
+-------+-------+-------+
|               |       |
v               v       v

Secret       Config     CVE
Detector     Analyzer   Scanner

        |
        v

Risk Analyzer

        |
+-------+----------+
|                  |
v                  v

Report          Database
Generator       Storage

                   |
                   v

             Scan History
             Dashboard