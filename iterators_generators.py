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