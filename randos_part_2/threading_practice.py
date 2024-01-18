import threading
import time
import random

def print_names():
    for name in ("Peter", "Cassie", "Mickie", "Josie", "Walker"):
        print(name)
        time.sleep(random.uniform(0.5, 1.5))

def print_age(min_sleep: float, max_sleep: float):
    for _ in range(5):
        print(random.randint(20, 50))
        time.sleep(random.uniform(min_sleep, max_sleep))

t1 = threading.Thread(target=print_names)
t2 = threading.Thread(target=print_age, args=(0.2, 1))

t1.start()
t2.start()

t1.join()
t2.join()
