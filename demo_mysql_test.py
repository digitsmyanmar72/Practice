import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="8000",
  database = "mydbone"
)

mycursor = mydb.cursor()
#  mycursor.execute("CREATE DATABASE mydbone")
#  mycursor.execute("CREATE TABLE customerstwo (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("Show databases")
mycursor.execute("Show tables")

for x in mycursor:
    print(x) 
    
'''sql = "INSERT INTO customerstwo (name, address) VALUES (%s, %s)"
val = [
 
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit() '''