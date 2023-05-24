from users import *
from custom_types import Gender
import tkinter as tk

def main():
    um = UserManager()
    um.ensure_table()

    user1 = User("Pena Penanen", Gender.MALE, 40, 40_000)
    print(um.add_user(user1))

if __name__ == "__main__":
    main()
