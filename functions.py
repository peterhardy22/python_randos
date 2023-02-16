# # Default parameter practice.
# def add(a: int, b: int) -> int:
#     return a + b

# def subtract(a: int, b: int) -> int:
#     return a - b

# def math(a: int, b: int, func=add) -> int:
#     """Function uses a function as a parameter"""
#     return func(a, b)

# # print(math(2, 2))
# # print(math(2, 2, subtract))


# # Using dictionaries instead of long conditional.
# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"

# def speak(animal='dog'):
#     """"Example of using default argument in dict.get()"""
#     noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
#     return noises.get(animal, '?')


# # Global variable scope.
# total: int = 0

# def increment() -> int:
#     """Example of using a variable in a function that is global"""
#     global total
#     total += 1
#     return total

# # Nonlocal scope.
# def outer() -> int:
#     """Example of using a variable with nonlocal scope"""
#     count: int = 0
#     def inner() -> int:
#         nonlocal count
#         count += 1
#         return count
#     return inner()

# # Retrieves a functions """ comments!
# # function_name.__doc__
# print(outer.__doc__)


# # flesh out multiple_letter count:
# def multiple_letter_count(string: str) -> dict:
#     """Example function that returns a dictionary of letters counted in a string"""
#     return {letter: string.count(letter) for letter in string}

# # multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}


# def list_manipulation(a_list: list, command: str, location: str, value: int=None) -> list:
#     """Example function for removing items from different parts of a list"""
#     if (command=="remove" and location=="end"):
#         return a_list.pop()
#     elif (command=="remove" and location=="beginning"):
#         return a_list.pop(0)
#     elif (command=="add" and location=="beginning"):
#         a_list.insert(0, value)
#     elif (command=="add" and location=="end"):
#         a_list.append(value)
#     return a_list

# # list_manipulation([1,2,3], "remove", "end") # 3
# # list_manipulation([1,2,3], "remove", "beginning") #  1
# # list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# # list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]


# def is_palindrome(string: str) -> bool:
#     """Classic palindrome function"""
#     return string == string[::-1]


# def intersection(list_1: list, list_2: list) -> list:
#     """Example function returns the intersection of two lists"""
#     return [element for element in list_1 if element in list_2]

# def intersection(list_1: list, list_2: list) -> list:
#     """Exampke function uses sets to return the intersection of 2 lists."""
#     return [element for element in set(list_1) & set(list_2)]


# def combine_words(word: str, **kwargs: dict) -> str:
#     """Example function that uses a paramter and kwargs"""
#     if 'prefix' in kwargs:
#         return kwargs['prefix'] + word
#     elif 'suffix' in kwargs:
#         return word + kwargs['suffix']

#     return word


# def unpacking_tuples(*args: tuple) -> int:
#     """Example function to display tuple unpacking by use of the * before the argument"""
#     total: int = 0
#     for num in args:
#         total += num
    
#     return total

# # nums: list = [1, 2, 3, 4, 5, 6]
# # unpacking_tuples(nums) #=> ([1, 2, 3, 4, 5, 6],) and errors out
# # unpacking_tuples(*nums) #=> (1, 2, 3, 4, 5, 6) runs correct
# # nums: tuple = (1, 2, 3, 4, 5, 6)
# # unpacking_tuples(nums) #=> ((1, 2, 3, 4, 5, 6),) and errors out
# # unpacking_tuples(*nums) #=> (1, 2, 3, 4, 5, 6) runs correct

from typing import Union

def calculate(**kwargs: dict) -> str:
    operation_lookup: dict = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float: bool = kwargs.get('make_float', False)
    operation_value: Union[int, float] = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final