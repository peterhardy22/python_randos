"""Tasked with trying to do mutliprocessing in a script."""
import multiprocessing

def square_sum(numbers: list) -> None:
    """Calculates the sum of squares of a list of numbers."""
    total: int = sum([num**2 for num in numbers])
    print(f"Sum of squares from {numbers=}: {total}")

numbers: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

chunk1 = numbers[:5]
chunk2 = numbers[5:]