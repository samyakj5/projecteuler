import math

num_primes = 10_000
is_prime = [False] + [False] + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if not is_prime[i]:
        continue
    for k in range(i * i, num_primes, i):
        is_prime[k] = False

list_primes = [x for x in range(num_primes) if is_prime[x]]

UL = 50_000_000
nums = set()

for c in list_primes:
    if c**4 > UL:
        break
    for b in list_primes:
        if c**4 + b**3 > UL:
            break
        for a in list_primes:
            if c**4 + b**3 + a**2 > UL:
                break
            nums.add(c**4 + b**3 + a**2)

print(len(nums))