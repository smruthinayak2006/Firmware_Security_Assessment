import hashlib



def calculate_hash(file_path):


    result = {


        "md5": "",

        "sha256": ""


    }



    try:



        md5 = hashlib.md5()

        sha256 = hashlib.sha256()




        with open(

            file_path,

            "rb"

        ) as firmware:



            while True:



                data = firmware.read(4096)



                if not data:


                    break



                md5.update(data)

                sha256.update(data)






        result["md5"] = md5.hexdigest()


        result["sha256"] = sha256.hexdigest()






    except Exception as error:



        print(

            "Hash analysis failed:",

            error

        )






    return result