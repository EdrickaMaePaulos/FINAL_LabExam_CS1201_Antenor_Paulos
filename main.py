from datetime import datetime
from user_manager import UserManager
from dice_game import DiceGame
import os

class Menu(UserManager):
  def __init__(self):
    pass

  def main():
    print ("\nWelcome to Dice Roll Game!")
    print ("\n1. Register")
    print ("2. Log in")
    print ("3. Exit")

    choice = int(input("Enter your choice: "))
    while True:
      try: 
        pass
      except ValueError as e:
        print (e)
        Menu.main()
          


