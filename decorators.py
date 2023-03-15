def shout(func: function) -> str:
    def wrapper(*args, **kwargs):
        """
        Wrapper function that returns string in uppercase.
        """
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

print(greet("todd"))
print(order(side="burger", main="fries"))
print(lol())
