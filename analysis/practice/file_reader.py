import os


folder_path = "sample_firmware"


keywords = [
    "password",
    "username",
    "secret",
    "key"
]


for filename in os.listdir(folder_path):

    file_location = os.path.join(
        folder_path,
        filename
    )


    with open(file_location, "r") as file:
        content = file.read()


    for keyword in keywords:

        if keyword in content.lower():

            print(
                "Possible secret found in:",
                filename
            )

            print(
                "Keyword:",
                keyword
            )