import json

from datetime import datetime


def generate_report(
    results,
    summary,
    firmware,
    firmware_hash
):


    report = {


        "report_information": {


            "generated_time": str(
                datetime.now()
            ),


            "tool": "Automated Firmware Security Assessment"


        },


        "firmware_information": firmware,


        "firmware_integrity": firmware_hash,


        "risk_summary": summary,


        "vulnerabilities": results


    }



    with open(
        "reports/security_report.json",
        "w"
    ) as file:


        json.dump(

            report,

            file,

            indent=4

        )



    return report