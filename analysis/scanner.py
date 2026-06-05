import os


KEYWORDS = [
    "password",
    "username",
    "secret",
    "key"
]


def scan_firmware(folder_path):

    findings = []


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


                for keyword in KEYWORDS:

                    if keyword in content.lower():

                        findings.append(
                            {
                                "file": file_path,
                                "issue": keyword
                            }
                        )


            except Exception as error:

                print(
                    "Could not scan:",
                    file_path
                )


    return findings



results = scan_firmware(
    "sample_firmware"
)


for result in results:

    print(result)