import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="eeli",
  password="hessuhopo",
  database="eeli"
)

# Mahdollistaa SQL suorituksen
mycursor = mydb.cursor()

