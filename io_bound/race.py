# io_bound/race.py
from concurrent.futures import ThreadPoolExecutor
counter = 0

def change_counter(amount):
    global counter
    for _ in range(10000):
        counter += amount

def race(num_threads):
    global counter
    counter = 0
    data = [-1 if x %2 else 1 for x in range(1000)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(change_counter, data)

    print(counter)
