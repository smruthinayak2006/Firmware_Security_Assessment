import sys
import os

sys.path.append(
    os.path.abspath("analysis")
)


from remediation import generate_recommendations




def test_remediation_generation():


    results = [

        {

            "finding": {

                "issue": "Telnet Enabled"

            }

        }

    ]




    output = generate_recommendations(

        results

    )




    assert "recommendation" in output[0]

    assert "SSH" in output[0]["recommendation"]