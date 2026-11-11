from mysql.connector import connect

con = connect(
    user="test",
    password="Test@123",
    host="localhost",
    database="weatherapi"
)

cursor = con.cursor()

id = int(input("enter your id: "))
title = input("enter your title: ")
status = input("enter status (True/False):").lower() == "true"

cursor.execute(
    "INSERT INTO tasks (id, title, status) VALUES (%s, %s, %s)",
    (id, title, status)
)

con.commit()
print("Task inserted successfully!")

cursor.close()
con.close()