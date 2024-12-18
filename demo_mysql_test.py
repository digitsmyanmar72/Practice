import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="8000",
  # database = "mydbone"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydbtwo")
mycursor.execute("Show databases")

for x in mycursor:
    print(x)