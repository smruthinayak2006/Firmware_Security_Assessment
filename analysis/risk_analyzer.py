def calculate_risk_summary(results):


    summary = {


        "total": len(results),

        "HIGH": 0,

        "MEDIUM": 0,

        "LOW": 0


    }



    for item in results:


        severity = item[
            "finding"
        ][
            "severity"
        ]



        if severity in summary:


            summary[
                severity
            ] += 1



    return summary