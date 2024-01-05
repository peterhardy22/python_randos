class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age) -> None:
        self.name = name
        self.job = job
        self.age = age

person1 = Person("Mickie", "Orchestrator", 4)
person2 = Person("Josie", "Free Spirit", 3)
person3 = Person("Josie", "Free Spirit", 3)
person4 = Person("Walker", "Plumper", 0)

print(id(person2))
print(id(person3))
print(person1)

print(person3 == person2)