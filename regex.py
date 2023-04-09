import re


email: str = "duder@dude.com"
result = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$", email)

if result:
  print("YES! We have an email address!")
else:
  print("Not a valid email address!")