"""Using pools for multiprocessing."""
import multiprocessing
import time


def is_prime(number: int) -> bool:
    """Checks if a number is prime."""
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    
    integer: int = 5
    while integer * integer <= number:
        if number % integer == 0 or number % (integer + 2) == 0:
            return False
        integer += 6
    return True

def find_primes(numbers: list) -> list:
    """Find all prime numbers in a list."""
    primes: list = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes


if __name__ == "__main__":
    numbers: list = list(range(100_000_000, 101_000_001))
    processes: int = 5
    
    chunk_size: float = len(numbers) // processes
    chunks: list = [numbers[integer : integer + chunk_size] for integer in range(0, len(numbers), chunk_size)]

    pool = multiprocessing.Pool(processes=processes)
    start_time = time.monotonic()

    results = pool.map(find_primes, chunks)

    primes: list = []
    for result in results:
        primes += result

    pool.close()
    pool.join()

    end_time = time.monotonic()

    print(
        f"Found {len(primes):,} prime numbers "
        f"between {numbers[0]:,} and {numbers[-1]:,} "
        f"in {(end_time - start_time):.2f} seconds."
    )
