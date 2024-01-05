"""
    - order=True allows you to be able to compare objects (ex. person1>person2).
        - sort_index: int allows you to sort on an int such as age.
        - import field and field(init=False, repr=False) make it so it does not need to be initialized nor shown when printed.
"""

from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age

person1 = Person("Mickie", "Orchestrator", 4)
person2 = Person("Josie", "Free Spirit", 3)
person3 = Person("Josie", "Free Spirit", 3)
person4 = Person("Walker", "Plumper", 0)

print(id(person2))
print(id(person3))
print(person1)

print(person1<person2)