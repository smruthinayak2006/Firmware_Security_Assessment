import json



def check_cve(content):


    findings = []


    with open(
        "database/cve_database.json",
        "r"
    ) as file:


        database = json.load(file)



    content = content.lower()



    for component, details in database.items():


        if component in content:


            findings.append(

                {

                    "issue": "Known Vulnerable Component",

                    "component": component,

                    "cve": details["cve"],

                    "name": details["name"],

                    "severity": details["severity"]

                }

            )



    return findings