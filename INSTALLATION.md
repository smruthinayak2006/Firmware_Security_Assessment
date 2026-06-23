\# Installation Guide



\## Automated Firmware Security Assessment



This guide explains how to set up and run the firmware security scanner locally.





\## Requirements



\- Python 3

\- Git

\- pip package manager





\## Clone Repository



```bash

git clone <repository-url>



cd firmware\_security\_assessment

```





\## Create Virtual Environment



```bash

python -m venv venv

```





Activate environment:



Windows:



```bash

venv\\Scripts\\activate

```





Linux:



```bash

source venv/bin/activate

```





\## Install Dependencies



```bash

pip install -r requirements.txt

```





\## Run Application



```bash

python app/app.py

```





Open:



http://127.0.0.1:5000





\## Application Workflow



1\. Login using authorized credentials



2\. Upload firmware



3\. System performs:



\- Firmware analysis

\- Vulnerability scanning

\- CVE detection

\- Hash verification

\- Risk calculation

\- Remediation generation





4\. Download security report







\## Testing



Run:



```bash

pytest

```





Expected:



All security module tests should pass.







\## Optional Firmware Extraction Support



For advanced firmware filesystem extraction install:



Binwalk





Without Binwalk:



The application automatically performs direct firmware scanning.

