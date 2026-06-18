import sqlite3

from datetime import datetime



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

            severity TEXT,

            scan_time TEXT

        )

        """

    )



    connection.commit()


    connection.close()








def save_results(results):


    create_database()



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

                severity,

                scan_time

            )

            VALUES(?,?,?,?)

            """,



            (

                item["file"],

                item["finding"]["issue"],

                item["finding"]["severity"],

                str(datetime.now())

            )

        )





    connection.commit()



    connection.close()









def get_scan_history():



    create_database()



    connection = sqlite3.connect(
        DB_NAME
    )


    cursor = connection.cursor()




    cursor.execute(

        """

        SELECT

        filename,

        issue,

        severity,

        scan_time

        FROM scans

        ORDER BY id DESC

        """

    )




    history = cursor.fetchall()



    connection.close()



    return history