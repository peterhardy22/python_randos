def week() -> str:
    """
    Returns a day of the week until the end of the week.
    """
    days: list = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        yield day 


def yes_or_no() -> str:
    """
    Returns yes if no was the previous response and vice versa.
    """
    answer: str = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


def current_beat() -> int:
    """
    Returns a standard beat count infinitly.
    """
    numbers: tuple = (1, 2, 3, 4)
    index: int = 0

    while True:
        if index >= len(numbers): index = 0
        yield numbers[index]
        index += 1


def make_song(verses: int = 99, beverage: str = "soda") -> str:
    """
    99 Bottles of {beverage} on the wall song in code.
    """
    for number in range(verses, -1, -1):
        if number > 1:
            yield "{number} bottles of {beverage} on the wall."
        elif number == 1:
            yield "Only 1 bottle of {beverage} left!"
        else:
            yield "No more {beverage}!"


def get_multiples(number: int = 1, count: int = 10) -> int:
    """
    Returns multiples of a number up to a certain amount of times.
    """
    next_number: int = number
    while count > 0:
        yield next_number
        count -= 1
        next_number += number


def get_unlimited_multiples(number: int = 1) -> int:
    """
    Returns an infinite amount of multiples for a given number.
    """
    next_number: int = number
    while next_number:
        yield next_number
        next_number += number

# sevens = get_unlimited_multiples(7)
# [next(sevens) for i in range(15)] 
# # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

# ones = get_unlimited_multiples()
# [next(ones) for i in range(20)]
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]