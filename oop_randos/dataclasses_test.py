"""
    - order=True - Allows you to be able to compare objects (ex. person1>person2).
        - sort_index: int - Allows you to sort on an int such as age.
        - import field and field(init=False, repr=False) - Make it so it does not need to be initialized nor shown when printed.
    - frozen=True - Creates objects that are read only.
        - object.__setattr__(self, "sort_index", self.strength) - Circumvents the dataclass being frozen.
        
"""

from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self) -> None:
        object.__setattr__(self, "sort_index", self.strength)
        
    def __str__(self) -> str:
        return f"{self.name} ({self.age}) is a {self.job}."

person1 = Person("Mickie", "Orchestrator", 4, 95)
person2 = Person("Josie", "Free Spirit", 3)
person3 = Person("Josie", "Free Spirit", 3)
person4 = Person("Walker", "Plumper", 0)

print(id(person2))
print(id(person3))
print(person1)

print(person1>person2)