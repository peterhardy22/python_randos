def shout(func: function) -> str:
    def wrapper(*args, **kwargs):
        """Wrapper function that returns string in uppercase."""
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name: str) -> str:
    return f"Hi, I'm {name}."

@shout
def order(main: str, side: str) -> str:
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol() -> str:
	return "lol"

# print(greet("todd"))
# print(order(side="burger", main="fries"))
# print(lol())


from functools import wraps

def log_function_data(func: function) -> int:
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I am the wrapper function."""
        print(f"you are about to call {func.__name__}")
        print(f"Here's the documentation: {func.__doc__}")
        return func(*args, **kwargs)
    return wrapper


@log_function_data
def add(x: int, y: int) -> int:
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)
help(add)