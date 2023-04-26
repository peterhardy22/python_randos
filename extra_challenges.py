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