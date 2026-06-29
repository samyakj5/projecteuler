import math

num_primes = 1_000_000
is_prime = [False] + [False] + [True] * (num_primes - 2)

for i in range(0, num_primes):
    if not is_prime[i]:
        continue
    for k in range(2 * i, num_primes, i):
        is_prime[k] = False

max_pair = (1, 41)
max_n = 40

for a in range(-1000, 1000):
    for b in range(2, 1000):
        if not is_prime[b]:
            continue
        n = 0
        while is_prime[n**2 + a * n + b]:
            n += 1
        if n > max_n:
            max_pair = (a, b)
            max_n = n

print(math.prod(max_pair))