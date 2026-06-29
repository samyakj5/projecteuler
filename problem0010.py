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

n = 2
p_sum = 0

while n < 2000000:
    if is_prime(n):
        p_sum += n
        print(n)

    n += 1

print(p_sum)
    

