import re


PATTERNS = {

    "Hardcoded Password": {
        "regex": r"password\s*=\s*\w+",
        "severity": "HIGH"
    },


    "API Key": {
        "regex": r"api[_-]?key\s*=\s*\w+",
        "severity": "HIGH"
    },


    "Secret Token": {
        "regex": r"secret\s*=\s*\w+",
        "severity": "MEDIUM"
    }

}



def detect_secrets(content):

    findings = []


    for name, rule in PATTERNS.items():


        matches = re.findall(
            rule["regex"],
            content,
            re.IGNORECASE
        )


        if matches:

            findings.append(
                {
                    "issue": name,
                    "severity": rule["severity"],
                    "matches": matches
                }
            )


    return findings

sample = """

username=root
password=root123
api_key=ABC12345

"""


result = detect_secrets(sample)


print(result)