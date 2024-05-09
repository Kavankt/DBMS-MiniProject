import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="nikhil",
   password="Nikhil@11"
)

c = mydb.cursor()
c.execute("CREATE DATABASE petroltry")