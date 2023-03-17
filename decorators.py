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

# print(sum_nums_gen())
# print(sum_nums_list())

 
def show_args(func) -> str:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass

# do_nothing(1, 2, 3,a="hi",b="bye")


def ensure_fewer_than_three_args(func: function):
    wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return func(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)

# add_all() # 0
# add_all(1) # 1
# add_all(1,2) # 3
# add_all(1,2,3) # "Too many arguments!"
# add_all(1,2,3,4,5,6) # "Too many arguments!"


def only_ints(func: function):
    wraps(func)
    def wrapper(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return func(*args, **kwargs)
    return wrapper

# @only_ints 
# def add(x, y):
#     return x + y
    
# add(1, 2) # 3
# add("1", "2") # "Please only invoke with integers."


