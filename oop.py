class User:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self.age = age

    def full_name(self) -> str:
        return f"{self.first} {self.last}"

user1 = User("Peter", "Hardy", 34)
print(user1.full_name())