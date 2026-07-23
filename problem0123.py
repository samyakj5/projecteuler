import math

num_primes = 1_000_000
is_prime = [False] * 2 + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

primes = [x for x in range(num_primes) if is_prime[x]]

UL = 10_000_000_000

for i in range(len(primes)):
    n = i + 1
    p = primes[i]
    a = p - 1
    b = p + 1
    s = (pow(a, n, p**2) + pow(b, n, p**2)) % p**2

    if s > UL:
        print(n)
        break