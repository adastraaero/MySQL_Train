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

my_list = [("Michael", "Vatutin", "145555", "keks@chpoks.ru", "Bibirevo",), ("Samantha", "Smith", "158585", "anus@vanus.pu", "Vasuki")]
sql = "INSERT INTO people (name, lastname, telephone, email, address) VALUES(%s, %s, %s, %s, %s)"

try:
    cur.executemany(sql, my_list)
    conn.commit()

except:
    conn.rollback()


cur.execute("SELECT * FROM people")
for x in cur:
    print(x)
    print("-" * 79)

cur.close()
conn.close()