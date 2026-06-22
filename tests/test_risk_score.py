import sys
import os

sys.path.append(
    os.path.abspath("analysis")
)


from risk_score import calculate_security_score



def test_high_risk_score():


    results = [

        {

            "finding": {

                "severity": "HIGH"

            }

        }

    ]



    score = calculate_security_score(

        results

    )



    assert score["raw_score"] == 30

    assert score["risk_level"] == "MEDIUM"