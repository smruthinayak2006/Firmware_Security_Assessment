import os

from secret_detector import detect_secrets
from config_analyzer import analyze_config
from report_generator import generate_report


def scan_firmware(folder_path):

    results = []


    for root, folders, files in os.walk(folder_path):


        for file in files:


            file_path = os.path.join(
                root,
                file
            )


            try:

                with open(
                    file_path,
                    "r",
                    errors="ignore"

                ) as f:

                    content = f.read()



                secret_results = detect_secrets(
                    content
                )


                config_results = analyze_config(
                    content
                )


                all_findings = (
                    secret_results
                    +
                    config_results
                )



                for finding in all_findings:


                    results.append(

                        {
                            "file": file_path,
                            "finding": finding
                        }

                    )



            except Exception:

                continue


    return results



results = scan_firmware(
    "sample_firmware"
)



for result in results:

    print(result)


message = generate_report(results)


print(message)