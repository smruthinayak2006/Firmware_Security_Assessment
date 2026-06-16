import os
import hashlib
from datetime import datetime



def analyze_firmware(file_path):


    firmware_info = {}


    firmware_info["name"] = os.path.basename(
        file_path
    )


    firmware_info["size"] = os.path.getsize(
        file_path
    )


    firmware_info["scan_time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )



    sha256_hash = hashlib.sha256()


    with open(file_path, "rb") as file:


        while chunk := file.read(4096):


            sha256_hash.update(
                chunk
            )



    firmware_info["sha256"] = sha256_hash.hexdigest()



    return firmware_info