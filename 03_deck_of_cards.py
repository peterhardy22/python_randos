class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
    
    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        suits: list = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values: list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards: list = [Card(value, suit) for suit in suits for value in values]
    
    def __repr__(self) -> str:
        return f"Deck of {self.count()} cards."
    
    def count(self) -> int:
        return len(self.cards)
    
    def _deal(self, number) -> str:
        count: int = self.count()
        actual: int = min([count, number])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards: str = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards