import mysql.connector
from datetime import datetime
from connection import connection

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Efehan33!",
    database="school_database"
)

mycursor= connection.cursor()
sql="INSERT INTO student(StudentNumber,StudentName,StudentSurname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
students=[
   ("101","Abraham","Sweetvoice",datetime(2002,2,13),"M"),
   ("102","Omar","Nickson",datetime(2000,6,1),"F")
]

mycursor.executemany(sql,students)

try:
    connection.commit()
    print(f'{mycursor.rowcount} record is added to list')
except mysql.connector.Error as err:
    print('Error:',err)
finally:
    connection.close()