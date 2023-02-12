# Default parameter practice.
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def math(a: int, b: int, func=add) -> int:
    return func(a, b)

# math(2, 2)
# math(2, 2, subtract)