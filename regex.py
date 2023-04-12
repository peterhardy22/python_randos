import re


# Regex for an email.
# email: str = "duder@dude.com"
# result = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$", email)
# if result:
#   print("YES! We have an email address!")
# else:
#   print("Not a valid email address!")


# Regex for a phone number.
# phone_pattern = re.compile(r"\d{3} \d{3}-\d{4}")
# result_1 = phone_pattern.search("Call me at 415 555-4242!")
# result_2: list = phone_pattern.findall("Call me at 768 789-9845 or 634 523-2134")
# try:
#   print(result_1.group())
# except:
#   print("No phone number was found.")
# print(result_2)

phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")

def extract_phone(input: str) -> str:
    """Extracts all phone numbers found in a string."""
    match = phone_regex.search(input)
    if match:
      return match.group()
    return None


def extract_all_phones(input: str) -> list:
    """Extracts all phone numbers found in a string."""
    return phone_regex.findall(input)


def is_valid_phone(input: str) -> bool:
    """Checks if an entire string is a valid phone number."""
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.fullmatch(input)
    if match:
      return True
    return False


def is_valid_time(input: str) -> bool:
    """Determines if the input is formatted as a time."""
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False



url_regex = re.compile(r"(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
match = url_regex.search("http://www.youtube.com/videos/abc123")
# print(match.group())
# print(match.groups())
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))


def parse_bytes(input: str) -> list:
    """Returns a list of the binary bytes contained in the input string."""
    binary_regex = re.compile(r'\b[10]{8}\b')
    results: list = binary_regex.findall(input)
    return results
