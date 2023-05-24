import mysql.connector
import uuid
import tkinter as tk

mydb = mysql.connector.connect(
  host="localhost",
  user="eeli",
  password="hessuhopo",
  database="eeli"
)

# Mahdollistaa SQL suorituksen
mycursor = mydb.cursor()

class Gender:
  OTHER = '0'
  MALE = '1'
  FEMALE = '2'

class UserExistsException(Exception):
  "Raised when user already exists in a database"
  pass

class User:
  def __init__(self, name: str, gender: str, age: int, wealth: float) -> None:
    self.name = name
    self.gender = gender
    self.age = age
    self.wealth = wealth
    self.id = uuid.uuid5(uuid.NAMESPACE_DNS, self.name).__str__()
  def array(self):
    return [self.name, self.gender, self.age, self.wealth]

class UserManager:
  def ensure_table(self):
    mycursor.execute("CREATE TABLE IF NOT EXISTS pankkikayttajat (id VARCHAR(255) PRIMARY KEY, nimi VARCHAR(255), sukupuoli VARCHAR(2), ikä INT, varat INT)")

  def fetch_users(self):
    sql = "SELECT * FROM pankkikayttajat"
    mycursor.execute(sql)
    users = mycursor.fetchall()
    return users

  def add_user(self, user: User):
    # Check id (hash) not taken
    mycursor.execute("SELECT * FROM pankkikayttajat WHERE id = '%s'" % user.id)
    users_with_same_id = mycursor.fetchone()
    if (users_with_same_id is not None):
      return UserExistsException
    else:
      sql = "INSERT INTO pankkikayttajat (id, nimi, sukupuoli, ikä, varat) VALUES (%s, %s, %s, %s, %s)"
      mycursor.execute(sql, [user.id] + user.array())
      mydb.commit()

  def remove_user(self, user: User):
    sql = "DELETE FROM kayttajat WHERE id = %s"
    mycursor.execute(sql, user.id)
    mydb.commit()

  def modify_user(self, user: User):
    sql = "UPDATE pankkikayttajat SET nimi = %s, ikä = %s, sukupuoli = %s, varat = %s WHERE id = %s"
    mycursor.execute(sql, user.array() + [user.id])
    mydb.commit()

um = UserManager()
um.ensure_table()

user1 = User("Pena Penanen", Gender.MALE, 40, 40_000)
print(um.add_user(user1))
