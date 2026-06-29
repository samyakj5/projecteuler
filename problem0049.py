import math
from itertools import combinations

num_primes = 10_000
is_prime = [False] + [False] + [True] * (num_primes - 2)

for i in range(2, int(math.sqrt(num_primes))):
    if not is_prime[i]:
        continue
    for k in range(i * i, num_primes, i):
        is_prime[k] = False

prime_digit_counts = {}

ul = 10_000

for i in range(1_000, 10_000):
    if is_prime[i]:
        digits = tuple("".join(sorted(list(str(i)))))
        prime_digit_counts[digits] = prime_digit_counts.get(digits, [])
        prime_digit_counts[digits].append(i)
        if len(prime_digit_counts[digits]) >= 3:
            for combo in combinations(sorted(prime_digit_counts[digits]), 3): # better way
                if combo[2] - combo[1] == combo[1] - combo[0]:
                    print(str(combo[0]) + str(combo[1]) + str(combo[2]))

                

# for i in prime_digit_counts.values():
#     if len(i) >= 3:
#         print(i)
#         # i just brute forced and hand-computed the values from here until i found the right one