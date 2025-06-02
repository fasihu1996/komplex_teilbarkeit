import math
import time

STARTING_VALUE = 2
END_VALUE = 1000000000000000

# bisherige Ergebnisse: 56, 10.920, 2.118.480

def rechner(x):
    a = 3 * x + 1
    b = 4 * x + 1
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    if sqrt_a.is_integer() and sqrt_b.is_integer():
        print(f"Zahl {x}: Hurra sie ist komplexpraktisch, a: {a}, b: {b}, Wurzel a: {sqrt_a}, Wurzel b: {sqrt_b}")
        return x
    else:
        #print(f"Zahl {x}: Fail")
        return -1

results = set()
div3 = set()
start_time = time.time()

for i in range(STARTING_VALUE, END_VALUE):
    curr_res = rechner(i)
    if curr_res != -1:
        results.add(curr_res)

print(f"Komplexpraktisch: {sorted(results)}")

for i in range(len(results)):
    curr_num = results.pop()
    if not curr_num % 8:
        div3.add(curr_num)

print(f"Divisible by 3: {div3}")
end_time = time.time()
print(f"Laufzeit: {end_time - start_time:.2f} Sekunden")
