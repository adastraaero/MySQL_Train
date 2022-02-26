## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import time

import mysql.connector
#import mysql.connector as mysql
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
conn = mysql.connector.connect(
    host = "192.168.1.62",
    user = "username",
    passwd = "password",
    database = "test4"
)

cur = conn.cursor()

sql = "SELECT name, lastname FROM people UNION DISTINCT SELECT name, lastname FROM people_2"

try:
    cur.execute(sql)
    conn.commit()

except:
    conn.rollback()


cur.execute(sql)
for x in cur:
    print(x)
    print("-" * 79)

cur.close()
conn.close()