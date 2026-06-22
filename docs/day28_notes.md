# Day 28 - Testing and Validation


## Objective

Implemented automated testing to verify security modules and ensure application reliability.



## Problem

A working application interface does not guarantee that every internal module works correctly.

Future code changes may accidentally break existing functionality.



## Solution

Added automated unit testing using pytest.



## Testing Framework

Used:

pytest



Purpose:

- Execute automated tests
- Validate individual modules
- Detect failures early
- Improve software reliability



## Implemented Tests


### 1. Risk Score Testing

Test File:

tests/test_risk_score.py


Validated:

- Severity calculation
- Risk score generation
- Risk level classification



Example:

HIGH severity vulnerability generates expected risk points.



## 2. Remediation Engine Testing

Test File:

tests/test_remediation.py


Validated:

- Vulnerability identification
- Security recommendation mapping


Example:

Telnet vulnerability generates SSH based remediation guidance.



## 3. Hash Analyzer Testing

Test File:

tests/test_hash_analyzer.py


Validated:

- Firmware hash calculation
- MD5 generation
- SHA256 generation


Ensures firmware integrity verification works correctly.



## Why Unit Testing?


Unit testing verifies each module independently.


Benefits:

- Detects bugs early
- Prevents breaking existing features
- Supports future development
- Improves code reliability



## Regression Testing


Automated tests ensure new changes do not damage previously working functionality.


Example:

If risk scoring logic changes incorrectly, tests detect the failure.



## Test Execution


Command:


pytest



Successful Output:


3 passed



## Updated Structure


tests/

├── test_hash_analyzer.py

├── test_remediation.py

└── test_risk_score.py



## Status


Completed:

✔ Pytest integration

✔ Risk engine validation

✔ Remediation validation

✔ Hash analyzer validation

✔ Automated testing workflow