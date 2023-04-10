import re


# Regex for an email.
# email: str = "duder@dude.com"
# result = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$", email)
# if result:
#   print("YES! We have an email address!")
# else:
#   print("Not a valid email address!")


# Regex for a phone number.
phone_pattern = re.compile(r"\d{3} \d{3}-\d{4}")
result_1 = phone_pattern.search("Call me at 415 555-4242!")
result_2: list = phone_pattern.findall("Call me at 768 789-9845 or 634 523-2134")
try:
  print(result_1.group())
except:
  print("No phone number was found.")
print(result_2)