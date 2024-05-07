from utils.dice_game import DiceGame

class UserManager:
  def __init__(self, username, password):
    self.user_database = []
    self.username = username
    self.password = password

  def load_users():
    pass

  def save_users():
    pass

  def validate_username():
    pass

  def validate_password():
    pass

  def register():
    username = str(input("Enter your username: "))
    while True:
      try:
        if len(username) >= 4:
          username = UserManager.database[username]
          password = str(input("Enter password (Enter q to exit): "))
          while True:
            try:
              if len(password) >= 8:
                password = UserManager.database[password]
                choice = int(input("Enter 1 to return to menu: "))
                while True:
                  try:
                    if choice == 1:
                      DiceGame.play_game(username)
                    else:
                      print ("Invalid syntax. Please try again")
                      UserManager.register()
                  except ValueError as e:
                    print(e)
              else:
                print ("Password should be atleast 8 characters")
                UserManager.register()
            except ValueError as e:
              print(e)
      except ValueError as e:
        print (e)
        UserManager.register()
    

  def login():
    username = str(input("Enter your username, : "))
    password = str(input("Enter your password: "))

    if username in UserManager.user_database and UserManager.user_database[username][password] == password:
      pass


