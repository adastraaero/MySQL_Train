## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import time

import mysql.connector

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
conn = mysql.connector.connect(
    host = "172.17.50.105",
    user = "username",
    passwd = "password",
    database = "test4"
)

cur = conn.cursor()

while True:
    q = input("Type 'QUIT' to Break: ")
    if q == 'QUIT':
        print("Script Terminated")
        break

    id_to_delete = input("ID to Delete: ")

    sql = "DELETE FROM people where id = '{}'".format(id_to_delete)

    try:
        cur.execute(sql)
        conn.commit()

    except:
        conn.rollback()


cur.execute("SELECT * FROM people")
for x in cur:
    print(x)

cur.close()
conn.close()