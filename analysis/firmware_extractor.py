import os
import subprocess
import shutil


def extract_firmware(file_path):

    output_folder = "extracted_firmware"

    if os.path.exists(output_folder):

        shutil.rmtree(
            output_folder
        )


    os.makedirs(
        output_folder
    )


    if shutil.which("binwalk") is None:

        print(
            "Binwalk not installed. Direct firmware scanning enabled."
        )


        return os.path.dirname(
            file_path
        )


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
            "Firmware extraction failed:",
            error
        )


        return os.path.dirname(
            file_path
        )