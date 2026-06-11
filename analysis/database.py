import sqlite3



DB_NAME = "firmware_results.db"



def create_database():


    connection = sqlite3.connect(
        DB_NAME
    )


    cursor = connection.cursor()



    cursor.execute(
        """

        CREATE TABLE IF NOT EXISTS scans(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT,

            issue TEXT,

            severity TEXT

        )

        """
    )


    connection.commit()


    connection.close()





def save_results(results):


    connection = sqlite3.connect(
        DB_NAME
    )


    cursor = connection.cursor()



    for item in results:


        cursor.execute(

            """

            INSERT INTO scans(
                filename,
                issue,
                severity
            )

            VALUES(?,?,?)

            """,


            (

                item["file"],

                item["finding"]["issue"],

                item["finding"]["severity"]

            )

        )



    connection.commit()


    connection.close()