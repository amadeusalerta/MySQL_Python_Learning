import mysql.connector

def insertProduct(name,price,image,description):
 connection=mysql.connector.connect(host="localhost",user="root",password="Efehan33!",database="node-app")
 cursor=connection.cursor()
 
 sql="INSERT INTO products(name,price,image,description) VALUES(%s,%s,%s,%s)"
 values=(name,price,image,description)

 cursor.execute(sql,values)

 try:
  connection.commit()
  print(f'{cursor.rowcount} unit added')
  print(f'Last Added Unit ID:{cursor.lastrowid}')
 except mysql.connector.Error as Err:
  print('Error:',Err)
 finally:
  connection.close() 
  print("Database connection has closed.")

def insertProducts(list):
 connection=mysql.connector.connect(host="localhost",user="root",password="Efehan33!",database="node-app")
 cursor=connection.cursor()
 
 sql="INSERT INTO products(name,price,image,description) VALUES(%s,%s,%s,%s)"
 values=(list)

 cursor.executemany(sql,values)

 try:
  connection.commit()
  print(f'{cursor.rowcount} unit added')
  print(f'Last Added Unit ID:{cursor.lastrowid}')
 except mysql.connector.Error as Err:
  print('Error:',Err)
 finally:
  connection.close() 
  print("Database connection has closed.")

def getProducts():
  connection=mysql.connector.connect(host="localhost",user="root",password="Efehan33!",database="node-app")
  cursor=connection.cursor()

  cursor.execute('SELECT * FROM products')
  result=cursor.fetchall()
  for product in result:
   print(f'Name:{product[1]} Price: {product[2]}')
getProducts()