# Lambda function.
cube = lambda num: num ** 3


# Map.
def decrement_list(numbers: list) -> list:
    """Example function displaying use of map to take in a list aand decrement it by 1
    returning the list."""
    return list(map(lambda number: number - 1, numbers))


# Combing Map and Filter.
names: list = ["Peter", "Cassie", "Mickie", "Josie"]

example: list = list(map(lambda name: f"Your friend today is {name}",
            filter(lambda value: len(value) < 6, names)))
# print(example)


def remove_negatives(numbers: list) -> list:
    return list(filter(lambda number: number >= 0, numbers))