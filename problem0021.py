import math

def factor(n):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    factors.remove(n)

    return factors

amicable = set()

for a in range(2, 10000):
    b = sum(factor(a))
    if sum(factor(a)) == b and sum(factor(b)) == a and a != b:
        amicable.add(a)
        amicable.add(b)

print(sum(amicable))