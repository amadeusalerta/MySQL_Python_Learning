import mysql.connector

def getProducts():
  connection=mysql.connector.connect(host="localhost",user="root",password="Efehan33!",database="node-app")
  cursor=connection.cursor()

  cursor.execute('SELECT * FROM products')
  result=cursor.fetchall()
  for product in result:
   print(f'ID: {product[0]} Name:{product[1]} Price: {product[2]} Image: {product[3]} Description: {product[4]}')
getProducts()