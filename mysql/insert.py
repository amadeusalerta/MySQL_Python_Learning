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

list=[]
while True:
 name = input('Product name: ')
 price = float(input('Product price: '))
 image = input('Product image: ')
 description = input('Product description: ')

 list.append((name,price,image,description))

 result=input('Do you want to add more unit? (y/n)')
 if result=='n':
  print('Your new units has been added to Database')
  print(list)
  insertProducts(list)
  break
 

insertProduct(name,price,image,description)