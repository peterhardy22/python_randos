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