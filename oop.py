class User:
    active_users: int = 0

    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
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

user1 = User("Peter", "Hardy", 34)
print(user1.full_name())
print(user1.initials())


# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance
    
    def deposit(self, amount: float) -> float:
        """Adds provided amount to balance."""
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount: float) -> float:
        """Subtracts provided amount from balance."""
        self.balance -= amount
        return self.balance