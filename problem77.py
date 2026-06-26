import math

num_primes = 100
is_prime = [False] + [False] + [True] * (num_primes - 2)

for i in range(2, int(num_primes**0.5)):
    if not is_prime[i]:
        continue
    for k in range(i**2, num_primes, i):
        is_prime[k] = False

primes = [p for p in range(num_primes) if is_prime[p]]

ways = [1] + [0] * primes[-1]

for num in primes:
    for c in range(num, primes[-1]):
        ways[c] += ways[c - num]

for i in range(len(ways)):
    if ways[i] >= 5000:
        print(i)
        break