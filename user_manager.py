from dice_game import DiceGame

class UserManager:
  def __init__(self, username, password):
    self.user_database = [
    self.UserManager.username = 'username'
    self.UserManager.password = 'password'
    ]
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
        if len(username) == 4:
          password = str(input("Enter password (Enter q to exit): "))
          while True:
            try:
              pass
            except ValueError as e:
              print(e)
      except ValueError as e:
        print (e)
        UserManager.register()
    

  def login():
    username = str(input("Enter your username, : "))
    password = str(input("Enter your password: "))

    while True: 
      try:
        if len(username) == 4:
          if username in UserManager.user_database[username]:
            if len(password) == 8:
              if password == UserManager.password:

      except ValueError as e:
        print (e)
        UserManager.login()




