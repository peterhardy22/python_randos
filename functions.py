# Default parameter practice.
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def math(a: int, b: int, func=add) -> int:
    return func(a, b)

# math(2, 2)
# math(2, 2, subtract)


# Using dictionaries instead of long conditional.
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')


# Global variable scope.
total: int = 0

def increment() -> int:
    global total
    total += 1
    return total

# Nonlocal scope.
def outer() -> int:
    count: int = 0
    def inner() -> int:
        nonlocal count
        count += 1
        return count
    return inner()