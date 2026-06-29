import math

def factor(n):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    return factors

i = 2
num = 1

while True:
    if len(factor(num)) < 500:
        num += i
        i += 1
    else:
        print(num)
        break