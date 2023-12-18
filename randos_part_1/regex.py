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


def parse_name(input: str) -> str:
    """Function that takes in a name and parses first and last names."""
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.group())
    print(matches.group('first'))
    print(matches.group('last'))

# parse_name("Mrs. Tilda Swinton")

 
def parse_date(input: str) -> dict:
    """Function that checks if the input is a valid date format."""
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match: str = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None


# Without Verbose Flag...
# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	# first part of email.	
	@					# single @ sign.
	([0-9a-z\.-]+)		# email provider.
	\.					# single period.
	([a-z\.]{2,6})$		# com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)

# match = pattern.search("PeteR123@Yahoo.com")
# print(match.group())
# print(match.groups())


text: str = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# result: list = pattern.findall(text)
# result: str = pattern.search(text).group()
result = pattern.sub("\g<1> \g<2>", text)
print(result)


def censor(input: str) -> str:
    """This function detects if frack is in a word and censors it."""
    pattern = re.compile(r'\bfrack\w*\b', re.I)
    result: str = pattern.sub("CENSORED", input)
    return result