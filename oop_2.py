# Inheritance and super().
class Animal:
    def __init__(self, name: str, species: str) -> None:
        self.name: str = name
        self.species: str = species
    
    def __repr__(self) -> str:
        return f"{self.name} is a {self.species}."

    def make_sound(self, sound: str) -> str:
        """Returns the sound the animal makes based on the argument passed in."""
        print(f"This animal named {self.name} says {sound}!")

class Cat(Animal):
    def __init__(self, name: str, breed: str, toy: str) -> None:
        super().__init__(name, species="Cat")
        self.breed: str = breed
        self.toy: str = toy
    
    def play(self) -> str:
        print(f"{self.name} plays with {self.toy}!")

# # charlie = Cat("Charlie", "Russian Blue", "String")
# # print(charlie)
# # charlie.play()

# Advanced Inheritance.
class User:
    active_users: int = 0

    def __init__(self, first: str, last: str, age: int) -> None:
        self.first: str = first
        self.last: str = last
        self.age: int = age
        User.active_users += 1
    
    def __repr__(self) -> str:
        return f"This is {self.first} {self.last}. They are {self.age} years old."
    
    @classmethod
    def display_active_users(cls: object) -> str:
        """Returns count of current active users."""
        return f"There are currently {cls.active_users} active users."
    
    @classmethod
    def from_string(cls: object, data_str: str) -> object:
        """Takes in user data as a string and creates user."""
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))
    
    def logout(self) -> str:
        """Subtracts a user from active_users."""
        User.active_users -= 1
        return f"{self.first} had logged out."

    def full_name(self) -> str:
        """Returns first and last name of user."""
        return f"{self.first} {self.last}"
    
    def initials(self) -> str:
        """Returns first intiial of users full name."""
        return f"{self.first[0]}.{self.last[0]}."

class Moderator(User):
    active_moderators: int = 0

    def __init__(self, first: str, last: str, age: int, community: str) -> None:
        super().__init__(first, last, age)
        self.community: str = community
        Moderator.total_moderators += 1
    
    @classmethod
    def display_active_moderators(cls: object) -> str:
        """Returns count of current active moderators."""
        return f"There are currently {cls.total_moderators} active moderators."
    
    def remove_post(self) -> str:
        """Alerts on who removed a post and from which community."""
        return f"{self.full_name()} removed a post from the {self.community} community."

# jasmine = Moderator("Jasmine", "O'Conner", 61, "Piano")
# johnny = User("Johnny", "Tsunami", 16)
# jimmy = User("Jimmy", "Butler", 30)
# print(User.display_active_users())
# print(Moderator.display_active_moderators)

from copy import copy

class Human:
    def __init__(self, first: str, last: str, age: int) -> None:
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self) -> str:
        return f"Human named {self.first} {self.last} that is aged {self.age} years old."
    
    def __len__(self) -> int:
        """Returns the age (length) of the human."""
        return self.age
    
    def __add__(self, other_human: object) -> int | str:
        """Function for 2 humans to be added together to create a baby."""
        if isinstance(other_human, Human):
            return Human(first="Baby", last=self.last, age=0)
        return "You can't add that with another human!"
    
    def __mul__(self, other_human: object) -> list:
        """Allows humans to multiply!"""
        if isinstance(other_human, int):
            return [copy(self) for human in range(other_human)]
        return "You can't multiply that!"


class GrumpyDict(dict):
    def __repr__(self) -> dict:
        print("None of your business!")
        return super().__repr__()

    def __missing__(self, key: str) -> None:
        """Function used for when a key that is missing comes up."""
        print(f"You want {key}? Well it ain't here!")

    def __setitem__(self, key: str, value: str) -> dict:
        print("You want to change the dictionary?!")
        print("Ughhh... Fine...")
        super().__setitem__(key, value)
    