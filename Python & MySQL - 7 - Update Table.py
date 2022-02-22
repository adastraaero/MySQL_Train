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

print("Custom MySQL ID Updater v0.1 \n")
print("-" * 79)


while True:
    cur.execute("SELECT * FROM people")
    for x in cur:
        print(x)

    q = input("Type 'QUIT' to Break, 'ENTER' to Continue: ")
    if q == 'QUIT':
        print("Script Terminated")
        break

    k_id = input("ID: ")
    k_name = input("Name: ")
    k_telephone = input("Telephone: ")
    k_email = input("Email: ")
    k_address = input("Address: ")


    sql = """UPDATE people SET name = '{1}', telephone = '{2}', email = '{3}', address = '{4}' WHERE id = '{0}'""".format(k_id, k_name, k_telephone, k_email, k_address)

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