# Default parameter practice.
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def math(a: int, b: int, func=add) -> int:
    """Function uses a function as a parameter"""
    return func(a, b)

# print(math(2, 2))
# print(math(2, 2, subtract))


# Using dictionaries instead of long conditional.
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

def speak(animal='dog'):
    """"Example of using default argument in dict.get()"""
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')


# Global variable scope.
total: int = 0

def increment() -> int:
    """Example of using a variable in a function that is global"""
    global total
    total += 1
    return total

# Nonlocal scope.
def outer() -> int:
    """Example of using a variable with nonlocal scope"""
    count: int = 0
    def inner() -> int:
        nonlocal count
        count += 1
        return count
    return inner()

# Retrieves a functions """ comments!
# function_name.__doc__
print(outer.__doc__)


# flesh out multiple_letter count:
def multiple_letter_count(string):
    """Example function that returns a dictionary of letters counted in a string"""
    return {letter: string.count(letter) for letter in string}

# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}


def list_manipulation(a_list, command, location, value=None):
    """Example function for removing items from different parts of a list"""
    if (command=="remove" and location=="end"):
        return a_list.pop()
    elif (command=="remove" and location=="beginning"):
        return a_list.pop(0)
    elif (command=="add" and location=="beginning"):
        a_list.insert(0, value)
    elif (command=="add" and location=="end"):
        a_list.append(value)
    return a_list

# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") #  1
# list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]


def is_palindrome(string):
    """Classic palindrome function"""
    return string == string[::-1]


def intersection(list_1, list_2):
    """Example function returns the intersection of two lists"""
    return [element for element in list_1 if element in list_2]

def intersection(list_1, list_2):
    """Exampke function uses sets to return the intersection of two lists."""
    return [element for element in set(list_1) & set(list_2)]