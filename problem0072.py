import math
from collections import Counter

UL = 1_000_000
p = list(range(UL + 1))

for i in range(2, math.isqrt(UL) + 1):
    if p[i] == i:
        for j in range(i * i, UL + 1, i):
            if p[j] == j:
                p[j] = i

def factorize(n):
    factors = []
    while n > 1:
        factors.append(p[n])
        n = n // p[n]

    return Counter(factors)

def totient(factors):
    return math.prod([pow(p, k-1) * (p - 1) for p, k in factors.items()])

r = 0

for i in range(2, UL + 1):
    factors = factorize(i)
    x = totient(factors)
    r += x

print(r)