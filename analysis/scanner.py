import os

from secret_detector import detect_secrets
from config_analyzer import analyze_config
from cve_checker import check_cve


def analyze_file(file_path):

    findings = []


    try:

        with open(
            file_path,
            "r",
            errors="ignore"
        ) as file:


            content = file.read()



        findings.extend(
            detect_secrets(content)
        )


        findings.extend(
            analyze_config(content)
        )

        findings.extend(

            check_cve(content)

        )


    except Exception:

        pass


    return findings





def scan_firmware(path):

    results = []


    files_to_scan = []



    if os.path.isfile(path):

        files_to_scan.append(
            path
        )



    else:


        for root, folders, files in os.walk(path):


            for file in files:


                files_to_scan.append(

                    os.path.join(
                        root,
                        file
                    )

                )




    for file_path in files_to_scan:


        findings = analyze_file(
            file_path
        )


        for finding in findings:


            results.append(

                {

                    "file": file_path,

                    "finding": finding

                }

            )



    return results