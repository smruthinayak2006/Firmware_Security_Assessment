import subprocess
import os



def extract_firmware(file_path):


    try:


        subprocess.run(

            [
                "binwalk",
                "-e",
                file_path
            ],

            check=True

        )


        extracted_folder = (
            "_" 
            + os.path.basename(file_path)
            + ".extracted"
        )


        if os.path.exists(
            extracted_folder
        ):


            return extracted_folder



        return file_path



    except Exception:


        return file_path