import sympy

UL = 1_000_000

num = 0
i = 1

while sympy.primorial(i) <= UL:
    num = sympy.primorial(i)
    i += 1

print(num)