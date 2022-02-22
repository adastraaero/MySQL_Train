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

names = []

file = open("database-names.txt", "r")
file.close

for x in file.readlines():
    names.append(x)

print(names)

for y in names:
    cur.execute("CREATE DATABASE " + y)
    time.sleep(2)

#db_names = ["test1", "test2", "test3"]

#for db in db_names:
    #cur.execute("CREATE DATABASE " + db)

#for db in db_names:
    #cur.execute("DROP DATABASE " + db)


cur.execute("SHOW DATABASES")

for x in cur:
    print(x)

cur.close()
conn.close()
