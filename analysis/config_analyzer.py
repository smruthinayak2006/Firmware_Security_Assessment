CONFIG_RULES = {

    "Debug Mode Enabled": {
        "pattern": "debug=true",
        "severity": "MEDIUM"
    },


    "Telnet Enabled": {
        "pattern": "telnet_enabled=true",
        "severity": "HIGH"
    },


    "Encryption Disabled": {
        "pattern": "encryption=false",
        "severity": "HIGH"
    }

}



def analyze_config(content):

    findings = []


    for issue, rule in CONFIG_RULES.items():


        if rule["pattern"] in content.lower():


            findings.append(

                {
                    "issue": issue,
                    "severity": rule["severity"]
                }

            )


    return findings

