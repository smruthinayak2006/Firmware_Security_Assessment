import json

from datetime import datetime





def generate_report(

    results,

    summary,

    firmware,

    firmware_hash,

    security_score

):




    report = {




        "report_information": {



            "generated_time": str(

                datetime.now()

            ),




            "tool": "Automated Firmware Security Assessment",



            "report_type": "IoT Firmware Security Analysis"



        },





        "firmware_information": firmware,





        "firmware_integrity": firmware_hash,





        "risk_summary": summary,





        "firmware_risk_score": security_score,





        "vulnerabilities": results,





        "security_recommendation": (

            "Review detected vulnerabilities, apply recommended fixes, "

            "and verify firmware before deployment."

        )




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