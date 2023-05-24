class Gender:
  OTHER = '0'
  MALE = '1'
  FEMALE = '2'

class UserExistsException(Exception):
  "Raised when user already exists in a database"
  pass

