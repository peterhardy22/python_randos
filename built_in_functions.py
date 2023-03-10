# # Lambda function.
# cube = lambda num: num ** 3


# # Map.
# def decrement_list(numbers: list) -> list:
#     """Example function displaying use of map to take in a list and decrement it by 1
#     returning the list."""
#     return list(map(lambda number: number - 1, numbers))


# # Combing Map and Filter.
# names: list = ["Peter", "Cassie", "Mickie", "Josie"]

# example: list = list(
#                     map(
#                         lambda name: f"Your friend today is {name}",
#                         filter(lambda value: len(value) < 6, names)
#                     )
#                 )
# # print(example)

# # Filter.
# def remove_negatives(numbers: list) -> list:
#     return list(filter(lambda number: number >= 0, numbers))


# # All and Any.
# def is_all_strings(items) -> bool:
#     """Example function determines whether all items in the iterable passed are strings."""
#     return all(type(item) == str for item in items)


# # Max and Abs.
# def max_magnitude(numbers) -> int:
#     """Example function using max to pick out largest int in a list."""
#     return max(abs(number) for number in numbers)


# # Sum.
# def sum_even_values(*args) -> int:
#     """Example function using sum to return total of all even numbers passed."""
#     return sum(arg for arg in args if arg % 2 == 0)


# def sum_floats(*args) -> float:
#     """Takes in any argument and returns only the sum of float data types."""
#     return sum(arg for arg in args if type(arg) == float)


# def interleave(string_1: str, string_2: str) -> str:
#     """Example function using zip to take in 2 strings and combine them into a single string."""
#     return "".join("".join(tup) for tup in zip(string_1, string_2))


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(dict_list: list) -> list:
    """Example function extracts and combines first and last name from list of dictionaries."""
    return list(map(lambda value: f"{value['first']} {value['last']}", dict_list))
