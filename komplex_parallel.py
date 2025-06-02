import math
import multiprocessing
import time

STARTING_VALUE = 2
END_VALUE = 1000000000000000


def rechner(x):
    if not x % 8 and not x % 7:
        a = 3 * x + 1
        b = 4 * x + 1
        sqrt_a = math.sqrt(a)
        sqrt_b = math.sqrt(b)
        if sqrt_a.is_integer() and sqrt_b.is_integer():
            return x
        else:
            return -1
    else:
        return -1

if __name__ == "__main__":
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = set()
        for res in pool.imap_unordered(rechner, range(STARTING_VALUE, END_VALUE), chunksize=10000):
            if res != -1:
                results.add(res)

    print(f"Komplexpraktisch: {sorted(results)}")
    div3 = {num for num in results if num % 8 == 0}
    print(f"Divisible by 3: {sorted(div3)}")
    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time:.2f} Sekunden")
