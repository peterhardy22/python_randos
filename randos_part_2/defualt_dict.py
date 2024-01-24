from collections import defaultdict


def default() -> int:
    """default_factory to assign 0 for any key that doesn not already exist for counting."""
    return 0

character_counter: dict = defaultdict(default)
test_string: str = "aaaaabbbbcdcdcdcdbbcccdeee"

for character in test_string:
    character_counter[character] += 1

print(character_counter)