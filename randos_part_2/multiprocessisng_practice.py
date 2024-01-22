"""Using pools for multiprocessing."""
import concurrent.futures
import multiprocessing
import random
import time


def compute_task(task_id, queue: int) -> float:
    """Perform a computationally intensive task."""
    count_to: int = queue.get()
    print(f"Starting task {task_id}. Counting up to {count_to:_}...")
    result: int = 0
    for integer in range(count_to):
        result += integer
    print(f"Finished task {task_id}.")
    return result


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        queue = manager.Queue()
        for _ in range(10):
            queue.put(random.randint(10_000_000, 50_000_000))
        
        start_time = time.monotonic()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures: list = [executor.submit(compute_task, t_id, queue) for t_id in range(10)]
            print("Submitted all tasks to the process pool.")
            results: list = []
            for index, future in enumerate(concurrent.futures.as_completed(futures)):
                print(f"Processing task {index + 1}/10...")
                result = future.result()
                print(f"Got result from task {index + 1}: {result:,}")
    
    print(f"Finished in {(time.monotonic() - start_time):.2f} seconds.")
