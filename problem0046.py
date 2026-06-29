import math

num_primes = 10_000
is_prime = [False] + [False] + [True] * (num_primes - 2)

for i in range(2, int(math.sqrt(num_primes))):
    if not is_prime[i]:
        continue
    for k in range(i * i, num_primes, i):
        is_prime[k] = False

ul = 10_000

for i in range(3, ul, 2):
    if not is_prime[i]:
        conj = True
        for j in range(1, int(math.sqrt(i)) + 1):
            if (i - 2 * j**2) <= 0:
                break
            if is_prime[i - 2 * j**2]:
                conj = False
                break
        if conj:
            print(i)
            break