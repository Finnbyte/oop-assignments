import uuid
import custom_types as types
import connection

class User:
  def __init__(self, name: str, gender: str, age: int, wealth: float) -> None:
    self.name = name
    self.gender = gender
    self.age = age
    self.wealth = wealth
    self.id = uuid.uuid5(uuid.NAMESPACE_DNS, self.name).hex
  def array(self):
    return [self.name, self.gender, self.age, self.wealth]

class UserManager:
  def ensure_table(self):
    connection.mycursor.execute("CREATE TABLE IF NOT EXISTS pankkikayttajat (id VARCHAR(255) PRIMARY KEY, nimi VARCHAR(255), sukupuoli VARCHAR(10), ikä INT, varat INT)")

  def fetch_users(self):
    sql = "SELECT * FROM pankkikayttajat"
    connection.mycursor.execute(sql)
    users = connection.mycursor.fetchall()
    return [User(user[1], user[2], user[3], user[4]) for user in users] if users is not None else [] 

  def add_user(self, user: User):
    # Check id (hash) not taken
    connection.mycursor.execute("SELECT * FROM pankkikayttajat WHERE id = '%s'" % user.id)
    users_with_same_id = connection.mycursor.fetchone()
    if (users_with_same_id is not None):
      return types.UserExistsException
    else:
      sql = "INSERT INTO pankkikayttajat (id, nimi, sukupuoli, ikä, varat) VALUES (%s, %s, %s, %s, %s)"
      connection.mycursor.execute(sql, [user.id] + user.array())
      connection.mydb.commit()

  def remove_user(self, user: User):
    connection.mycursor.execute("DELETE FROM pankkikayttajat WHERE id = '%s'" % user.id)
    connection.mydb.commit()

  def modify_user(self, user: User, new_user_data):
    sql = "UPDATE pankkikayttajat SET nimi = %s, ikä = %s, sukupuoli = %s, varat = %s WHERE id = %s"
    connection.mycursor.execute(sql, new_user_data + [user.id])
    connection.mydb.commit()

