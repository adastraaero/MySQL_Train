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

print(" MySQL Custom Client v0.1 \n")
print("-" * 79)

while True:
    q = input("Enter 'QUIT' to Break: ")
    if q == 'QUIT':
        break

    k_name = input("Name: ")
    k_telephone = input("telephone: ")
    k_email = input("email: ")
    k_address = input("address: ")

    sql = """INSERT INTO people(id, name, telephone, email, address)
    VALUES (NULL, '{}', '{}', '{}', '{}')""".format(k_name, k_telephone, k_email, k_address)



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