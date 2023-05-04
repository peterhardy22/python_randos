'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

def reverse_string(word: str) -> str:
    """Reverses given word."""
    return word[::-1]


'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(input_list: list) -> bool:
    """Determines if all elements in the given list are of the datatype list."""
    return all((isinstance(element, list) for element in input_list))


'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(input_list: list) -> list:
    """Returns the given lists' even number indexed items."""
    return [number for index, number in enumerate(input_list) if index % 2 == 0]


'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''
        
def sum_pairs(numbers_list: list, number: int) -> list:
    """Returns a list of the first numbers that sum together to make the input number."""
    already_visited: set = set()
    for additive in numbers_list:
        difference: int = number - additive
        if difference in already_visited:
            return [difference, additive]
        already_visited.add(additive)
    return []


'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(word: str) -> dict[str, int]:
    """Counts the occurence of vowels in a word."""
    lowercase_word: str = word.lower()
    return {letter: lowercase_word.count(letter) for letter in lowercase_word if letter in "aeiou"}


'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(sentence: str) -> str:
    """Capitalizes the first letter of every word in a sentence."""
    words_list: list = sentence.split(' ')
    answer_list: list = [word[0].upper() + word[1:] for word in words_list]
    return ' '.join(answer_list)


'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''

def find_factors(number: int) -> list[int]:
    """Returns a list of factors for a given number."""
    return [factor for factor in range(1, number + 1) if number % factor == 0]


'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(collection: dict | list | str, value: int, start: int =None):
    """Returns boolean depnding on if value is in collection taking into account given starting index."""
    if isinstance(collection, dict):
        return value in collection.values()
    if start is None:
        return value in collection
    return value in collection[start:]