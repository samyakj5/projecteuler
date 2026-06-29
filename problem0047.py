import math

num_primes = 1_000_000
is_prime = [False] * 2 + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

def prime_factorize(n):
    factors = set()
    while n > 1:
        if is_prime[n]:
            factors.add(n)
            return factors
        else:
            for i in range(2, math.ceil(math.sqrt(n)) + 1):
                if is_prime[i] and n % i == 0:
                    factors.add(i)
                    n = n // i
                    break

    return factors

n_k0 = set()
n_k1 = set()
n_k2 = set()
n_k3 = set()

for i in range(3, num_primes):
    n_k0, n_k1, n_k2 = n_k1, n_k2, n_k3
    n_k3 = prime_factorize(i)

    if len(n_k0) == len(n_k1) == len(n_k2) == len(n_k3) == 4:
        print(i - 3)
        break
        