# Lambda function.
cube = lambda num: num ** 3


# Map.
def decrement_list(numbers: list) -> list:
    """Example function displaying use of map to take in a list aand decrement it by 1
    returning the list."""
    return list(map(lambda number: number - 1, numbers))