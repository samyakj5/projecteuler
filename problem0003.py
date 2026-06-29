import math

def factors(num):
    factors = set()
    for i in range(math.ceil(math.sqrt(num))):
        if i == 0:
            continue
        if num % i == 0:
            factors.add(i)
            factors.add(num / i)
    return factors

prime_factors = set()

for i in range(math.ceil(math.sqrt(600851475143))):
    if i == 0:
        continue
    if 600851475143 % i == 0:
        if len(factors(i)) == 2:
            prime_factors.add(i)
            
print(max(prime_factors))