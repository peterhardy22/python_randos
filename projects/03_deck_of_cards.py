from random import shuffle

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
        """Counts the number of cards left in the current deck."""
        return len(self.cards)
    
    def _deal(self, number) -> str:
        """Deals out a certain number of cards based on what is passed in as an argument."""
        count: int = self.count()
        actual: int = min([count, number])
        if count == 0:
            raise ValueError("All cards have been dealt!")
        
        cards: str = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_card(self) -> str:
         """Deals out a single card."""
         return self._deal(1)[0]
    
    def deal_hand(self, hand_size: int) -> list:
        """Deals out a hand of cards based on the number passed in as the argument."""
        return self._deal(hand_size)
    
    def shuffle(self) -> list:
        if self.count() < 52:
            raise ValueError("Only full decks of 52 cards or more can be shuffled!")
        
        shuffle(self.cards)
        return self