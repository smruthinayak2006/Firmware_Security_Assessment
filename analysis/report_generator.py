import json
import os



def generate_report(results):


    os.makedirs(
        "reports",
        exist_ok=True
    )


    report_path = "reports/security_report.json"



    with open(
        report_path,
        "w"
    ) as file:


        json.dump(

            results,

            file,

            indent=4

        )


    return report_path     