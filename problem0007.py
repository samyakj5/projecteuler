import math

def factor(n):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    
    return factors

def is_prime(n):
    return len(factor(n)) == 2

i = 1
num = 2
while i < 10002:
    if is_prime(num):
        print(i, num)
        i += 1
    num += 1
