import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="80008000",
  
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase2")