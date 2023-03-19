from random import choice


def eat(food: str, is_healthy: bool) -> str:
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    ending: str = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"


def nap(hours: int) -> str:
    if hours >= 2:
        return f"Ugh I overslept.  I didn't mean to nap for {hours} hours!"
    return f"I'm feeling refreshed after my {hours} hour nap"


def is_funny(person: str) -> str:
    if person is 'tim':
        return False
    return True


def laugh() -> str:
    return choice(('lol', 'haha', 'tehehe'))
