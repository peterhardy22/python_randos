# Checks if a string contains every vowel.
string: str = 'sequoia'
answer: bool = len({character for character in string if character in 'aeiou'}) == 5