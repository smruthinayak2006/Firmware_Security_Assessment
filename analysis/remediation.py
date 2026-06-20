def generate_recommendations(results):


    fixes = {


        "Hardcoded Password":

        "Remove hardcoded credentials and use secure credential storage mechanisms.",



        "Debug Mode Enabled":

        "Disable debug mode before deploying firmware to production devices.",



        "Telnet Enabled":

        "Disable Telnet service and use encrypted SSH communication.",



        "Known Vulnerable Component":

        "Update vulnerable software components to patched versions."



    }




    for item in results:


        issue = item["finding"]["issue"]


        if issue in fixes:


            item["recommendation"] = fixes[issue]


        else:


            item["recommendation"] = (

                "Review firmware configuration and apply security best practices."

            )



    return results