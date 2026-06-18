## Day 17 - CVE Vulnerability Detection

### Concept

A CVE (Common Vulnerabilities and Exposures) represents a publicly known security vulnerability.

Firmware components should be checked against known vulnerabilities.


### Implementation

Modules:

analysis/cve_checker.py

database/cve_database.json


### Features Added

- Vulnerable component detection
- CVE identification
- Severity mapping


### Example

OpenSSL 1.0.1

Detected:

CVE-2014-0160 Heartbleed


### Learning Outcome

Understood how vulnerability scanners match software versions with known security issues.