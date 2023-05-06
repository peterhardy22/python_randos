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

def includes(collection: dict | list | str, value: int, start: int = None) -> bool:
    """Returns boolean depnding on if value is in collection taking into account given starting index."""
    if isinstance(collection, dict):
        return value in collection.values()
    if start is None:
        return value in collection
    return value in collection[start:]


'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(pete: int, repete: int) -> int:
    """Repeats the first argument repete amount of times."""
    return pete * repete


'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(sentence: str, number: int) -> str:
    """Truncates any given sentence up to the given amount of characters."""
    if number <= 2:
        return "Truncation must be at least 3 characters."
    if number > len(sentence):
        return sentence
    else:
        return f"{sentence[:(number - 3)]}..."


'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(keys_list: list, values_list: list) -> dict:
    """Combines 2 lists into a single dictionary."""
    answer_dict: dict = {}
    for index, _ in enumerate(keys_list):
        if index < len(values_list):
            answer_dict[keys_list[index]] = values_list[index]
        else:
            answer_dict[keys_list[index]] = None
    return answer_dict


'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''

def range_in_list(numbers_list: list, start: int = 0, end: int = None) -> int:
    """Returns the sum of the values  between the start and end indices of the given list."""
    if not end:
        end: int = len(numbers_list) - 1
    return sum(numbers_list[start:end+1])


'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(number_one: int, number_two: int) -> bool:
    """Returns True if both numbers have the same frequency of digits."""
    return len(str(number_one)) == len(str(number_two))


'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

def nth(numbers_list: list, number: int) -> int:
    """Returns the element in the given list at the provided index."""
    return numbers_list[number]


'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(numbers_list: list) -> int:
    """Searches for and returns the single duplicate number in the given list."""
    non_duplicates_list: list = []
    for number in numbers_list:
        if number not in non_duplicates_list:
            non_duplicates_list.append(number)
        else:
            return number


'''
EXAMPLES:

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]
sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
4 = ([0][0] + [1][1] + [2][2] + [3][3]) + ([0][3] + [1][2] + [2][1] + [3][0])
sum_up_diagonals(list4) # 68
'''

def sum_up_diagonals(numbers_list: list) -> int:
    """Returns the sum of the main diagonals in a NxN list of lists of numbers."""
    answer: int = 0
    
    for index, _ in enumerate(numbers_list):
        answer += numbers_list[index][index]
        answer += numbers_list[index][len(numbers_list) - index - 1]
    
    return answer

        
        
        
        
        
    