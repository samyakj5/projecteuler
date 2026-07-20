import math

num_primes = 100
is_prime = [False, False] + [True] * (num_primes - 2)

for i in range(2, math.isqrt(num_primes) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

primes = [x for x in range(num_primes) if is_prime[x]]



for prime in primes:
