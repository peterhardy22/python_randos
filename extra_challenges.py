'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

def reverse_string(word: str) -> str:
    """Reverses given word."""
    return word[::-1]