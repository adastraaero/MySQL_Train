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
    database = "datacamp"
)

cur = conn.cursor()

while True:
    run_this = input("MySQL Command: ")

    if run_this == 'QUIT':
        break

    try:
        cur.execute(run_this)
    except:
        conn.rollback()
    for x in cur:
        print(x)






cur.close()
conn.close()