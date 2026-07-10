import math

num_primes = 50
is_prime = [False, False] + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

primes = [x for x in range(num_primes) if is_prime[x]]

print(primes)

dp = [1] + [0] * num_primes
dp_map = {i : set() for i in range(0, num_primes + 1)}

for prime in primes:
    print(prime)
    dp_map[prime].add((prime, ))
    i = 1
    while prime + i <= num_primes:
        if dp_map[i]:
            for l in dp_map[i]:
                if prime not in l:
                    dp_map[prime + i].add(l + (prime, ))
        i += 1


for num in dp_map:
    print(num, dp_map[num], "\n")