class Gender:
  OTHER = 'Muu'
  MALE = 'Mies'
  FEMALE = 'Nainen'

class UserExistsException(Exception):
  "Raised when user already exists in a database"
  pass

