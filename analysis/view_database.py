import sqlite3



connection = sqlite3.connect(
    "firmware_results.db"
)



cursor = connection.cursor()



cursor.execute(

    "SELECT * FROM scans"

)



records = cursor.fetchall()



for record in records:


    print(record)



connection.close()