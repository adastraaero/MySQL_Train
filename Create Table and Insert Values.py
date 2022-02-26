## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import time

import mysql.connector

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
conn = mysql.connector.connect(
    host = "192.168.1.62",
    user = "username",
    passwd = "password",
    database = "test4"
)

cur = conn.cursor()

sql = '''CREATE TABLE people_2(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    lastname VARCHAR(70) NOT NULL,
    telephone INT,
    email VARCHAR(255),
    address VARCHAR(100)
)'''

try:
    cur.execute(sql)

except:
    conn.rollback()


cur.execute("DESCRIBE people_2")
for x in cur:
    print(x)




cur.close()
conn.close()