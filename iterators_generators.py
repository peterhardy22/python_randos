def week() -> str:
    days: list = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        yield day 