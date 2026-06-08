# Day 9 Notes


Implemented:

Firmware upload workflow


Learned:

- HTTP POST
- File upload handling
- Flask request object
- Connecting frontend with scanner


Architecture:

Browser

↓

Flask Upload

↓

Scanner Engine

↓

Security Results

## Current Limitation

The upload workflow is connected, but scanning currently runs on sample_firmware directory.

Upcoming improvement:
Uploaded firmware files will be extracted and scanned dynamically.