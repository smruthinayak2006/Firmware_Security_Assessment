import json
import os
from datetime import datetime


def generate_report(results):

    report = {

        "project":
            "Automated Firmware Security Assessment",

        "scan_time":
            str(datetime.now()),

        "total_findings":
            len(results),

        "findings":
            results
    }


    os.makedirs(
        "reports",
        exist_ok=True
    )


    with open(
        "reports/vulnerability_report.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    return "Report generated successfully"