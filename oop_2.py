# Inheritance.
class Animal:
    cool: bool = True

    def make_sound(self, sound: str) -> str:
        print(f"This animal says {sound}!")

class Cat(Animal):
    pass