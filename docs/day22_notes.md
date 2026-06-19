# Day 22 - Firmware Risk Scoring Engine

## Objective

Implemented a firmware risk scoring engine to calculate the overall security risk of uploaded IoT firmware based on detected vulnerabilities.


## Problem

Severity classification alone was not enough for firmware prioritization.

Example:

Firmware A:
- 1 High vulnerability

Firmware B:
- 5 High vulnerabilities

Both appear as HIGH severity, but Firmware B requires faster remediation.


## Solution

Implemented numerical risk scoring.


Severity Weight:

HIGH:
30 points

MEDIUM:
15 points

LOW:
5 points

The total score represents the overall firmware risk exposure.


## Risk Classification


0 - 19:
LOW Risk


20 - 49:
MEDIUM Risk


50 - 79:
HIGH Risk


80 - 100:
CRITICAL Risk


## Implementation


New Module:

analysis/risk_score.py



Responsibilities:

- Analyze vulnerability results
- Assign severity weights
- Calculate total risk score
- Classify firmware risk level


## Dashboard Integration


Added:

- Firmware risk score card
- Risk progress meter
- Risk level visualization
- SOC-style security dashboard


## Security Importance


Risk scoring helps security teams:

- Prioritize vulnerable firmware
- Identify critical devices faster
- Improve remediation decisions
- Track firmware security posture


## Status

Completed:

✔ Risk scoring engine

✔ Severity based weighting

✔ Risk classification

✔ Dashboard visualization

✔ SOC style interface