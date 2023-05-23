import mysql.connector
import tkinter as tk

mydb = mysql.connector.connect(
  host="localhost",
  user="eeli",
  password="hessuhopo",
  database="eeli"
)

# Mahdollistaa SQL suorituksen
mycursor = mydb.cursor()

class User:
    def __init__(self, name, gender, age, wealth) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.wealth = wealth
    def array(self):
        return [self.name, self.gender, self.age, self.wealth]
    def dict(self):
        return { "name": self.name, "gender": self.gender, "age": self.age, "wealth": self.wealth }

class UserManager:
    def setUser(self, user):
        self.user = user
    def fetch_all(self):
        sql = "SELECT * FROM pankkikayttajat"
        mycursor.execute(sql)
        users = mycursor.fetchall()
        return users
    def add_user(self, user):
        sql = "INSERT INTO pankkikayttajat (nimi, sukupuoli, ikä, varat) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql)
    def remove_user(self, user):
        sql = "INSERT INTO pankkikayttajat (nimi, sukupuoli, ikä, varat) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql)
    def modify_user(self, user):
        sql = "INSERT INTO pankkikayttajat (nimi, sukupuoli, ikä, varat) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql)
