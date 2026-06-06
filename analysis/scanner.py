import os

from secret_detector import detect_secrets



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


                findings = detect_secrets(
                    content
                )


                for finding in findings:


                    results.append(
                        {
                            "file": file_path,
                            "finding": finding
                        }
                    )



            except Exception:

                continue


    return results



scan_results = scan_firmware(
    "sample_firmware"
)



for item in scan_results:

    print(item)