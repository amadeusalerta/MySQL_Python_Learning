import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Efehan33!",
    database="mydatabase"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255),adress VARCHAR(255))")
