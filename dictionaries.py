# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"]. 
# Create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
list1: list = ["CA", "NJ", "RI"]
list2: list = ["California", "New Jersey", "Rhode Island"] 
# answer: dict = {list1[i]: list2[i] for i in range(0,3)}
# answer: dict = dict(zip(list1,list2))  


# Create a dictionary that makes each first item in each list a key and the second item a corresponding value. 
person: list = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer: dict = {rockstar[0]: rockstar[1] for rockstar in person}
# answer: dict = dict(person)


# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
# answer: dict = {character:0 for character in 'aeiou'}
# answer: dict = dict.fromkeys("aeiou", 0) 


# Create a dictionary that maps ASCII keys to their corresponding letters. 
# answer: dict = {number: chr(number) for number in range(65,91)} 