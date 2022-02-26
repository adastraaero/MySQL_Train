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
#sql = "ALTER TABLE people ADD COLUMN last_one VARCHAR(100)"
#sql = "ALTER TABLE people ADD COLUMN m_name VARCHAR(100) AFTER name"
#sql = "ALTER TABLE people ADD COLUMN custom_id INT FIRST"
#sql = "ALTER TABLE people ALTER last_one SET DEFAULT 'ULTRA Secret'"
#sql = "ALTER TABLE people ALTER last_one DROP DEFAULT"
sql = "ALTER TABLE people DROP COLUMN last_one"

try:
    cur.execute(sql)
    conn.commit()

except:
    conn.rollback()


cur.execute("SELECT * FROM people")
for x in cur:
    print(x)
    print("-" * 79)

cur.close()
conn.close()