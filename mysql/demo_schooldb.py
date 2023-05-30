import mysql.connector
from datetime import datetime

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Efehan33!",
    database="school_database"
)

mycursor=connection.cursor()

sql="INSERT INTO student(StudentNumber,StudentName,StudentSurname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
students=[
    ("103","Richard","Nixon",datetime(2001,7,10),"M"),
    ("104","Margareth","Thatcher",datetime(2004,11,9),"F")
]

mycursor.executemany(sql,students)

try:
    connection.commit()
    print(f'{mycursor.rowcount} record has been added.')
except mysql.connector.Error as err:
    print('Error',err)
finally:
    connection.close()