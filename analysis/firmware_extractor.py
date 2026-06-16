import os
import subprocess


def extract_firmware(file_path):

    output_folder = "extracted_firmware"


    if not os.path.exists(output_folder):

        os.makedirs(output_folder)


    try:

        subprocess.run(

            [
                "binwalk",
                "-e",
                file_path,
                "-C",
                output_folder
            ],

            check=True

        )


        return output_folder


    except Exception as error:

        print(
            "Binwalk extraction failed:",
            error
        )


        print(
            "Using original uploaded file"
        )


        return file_path