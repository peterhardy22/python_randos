from keyword import iskeyword

def contains_keyword(*args: str) -> bool:
    for string in args:
        if iskeyword(string): return True
    return False

