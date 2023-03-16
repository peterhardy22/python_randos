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

# print(add.__doc__)
# print(add.__name__)
# help(add)


# Let's define a speed_test decorator
from functools import wraps
from time import time

def speed_test(func: function) -> str:
	@wraps(func)
	def wrapper(*args, **kwargs):
		start_time = time()
		result: int = func(*args, **kwargs)
		end_time = time()
		print(f"Executing {func.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_gen() -> int:
	return sum(x for x in range(90000000))

@speed_test
def sum_nums_list() -> int:
	return sum([x for x in range(90000000)])


print(sum_nums_gen())
print(sum_nums_list())

