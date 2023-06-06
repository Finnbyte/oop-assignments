from enum import Enum, EnumMeta

# Allows us to inject custom methods into Enums
class CustomEnumMeta(EnumMeta): 
    def __contains__(cls, item): 
        return isinstance(item, cls) or item in [v.value for v in cls.__members__.values()] 

class Gender(Enum, metaclass=CustomEnumMeta):
  OTHER = 'Muu'
  MALE = 'Mies'
  FEMALE = 'Nainen'

class UserExistsException(Exception):
  "Raised when user already exists in a database"
  pass
