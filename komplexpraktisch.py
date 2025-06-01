import math

STARTING_VALUE = 2
END_VALUE = 100

def rechner(x):
    a = 3 * x + 1
    b = 4 * x + 1
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    if sqrt_a.is_integer() and sqrt_b.is_integer():
        print(f"Zahl {x}: Hurra sie ist komplexpraktisch, a: {a}, b: {b}, Wurzel a: {sqrt_a}, Wurzel b: {sqrt_b}")
    else:
        print(f"Zahl {x}: Fail")

for i in range(STARTING_VALUE, END_VALUE):
    rechner(i)