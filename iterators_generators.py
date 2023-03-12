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
    99 Bottles song in code.
    """
    for number in range(verses, -1, -1):
        if number > 1:
            yield "{number} bottles of {beverage} on the wall."
        elif number == 1:
            yield "Only 1 bottle of {beverage} left!"
        else:
            yield "No more {beverage}!"