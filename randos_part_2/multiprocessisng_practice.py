import multiprocessing


def square_sum(numbers: list) -> None:
    """Calculates the sum of squares of a list of numbers."""
    total: int = sum([num**2 for num in numbers])
    print(f"Sum of squares from {numbers=}: {total}")

if __name__ == '__main__':
    numbers: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    chunk1 = numbers[:5]
    chunk2 = numbers[5:]

    process1 = multiprocessing.Process(target=square_sum, args=(chunk1,))
    process2 = multiprocessing.Process(target=square_sum, args=(chunk2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()