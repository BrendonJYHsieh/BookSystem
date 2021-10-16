import mysql.connector

mydb = mysql.connector.connect(
  host="140.118.127.106",
  user="Manager",
  password="10815044",
  database="Booksystem"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)