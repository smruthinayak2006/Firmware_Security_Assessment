def calculate_security_score(results):


    raw_score = 0



    for item in results:


        severity = item[
            "finding"
        ][
            "severity"
        ]



        if severity == "HIGH":


            raw_score += 30



        elif severity == "MEDIUM":


            raw_score += 15



        elif severity == "LOW":


            raw_score += 5





    risk_score = min(
        raw_score,
        100
    )





    if risk_score >= 80:


        risk_level = "CRITICAL"



    elif risk_score >= 50:


        risk_level = "HIGH"



    elif risk_score >= 20:


        risk_level = "MEDIUM"



    else:


        risk_level = "LOW"






    return {


        "raw_score": raw_score,

        "risk_score": risk_score,

        "risk_level": risk_level


    }