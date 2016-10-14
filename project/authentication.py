from __future__ import print_function

def login(user_name, pass_word):
  try:
    user_file = open("users.txt")
    user_buf = user_file.read()
    users = [ line.split("|") for line in user_buf.split("\n")]
    if [user_name, pass_word] in users:
      return True
    else:
      return False
  except Exception, e:
    print("I can't autheticate you.")
    return False

def logout():
  print("This line will not be tested!")
  print("This line also won't be teseted!")

