# Inheritance.
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

charlie = Cat("Charlie", "Russian Blue", "String")
print(charlie)
charlie.play()