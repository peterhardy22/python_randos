from keyword import iskeyword

def contains_keyword(*args: str) -> bool:
    for string in args:
        if iskeyword(string): return True
    return False


from built_in_functions import extract_full_name

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))