# this code takes like 10 mins to run

import math

num_primes = 750_000_000
is_prime = [False, False] + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

num_primes = 0
total_nums = 0
curr_num = 1

UL = 30_000

for i in range(2, UL, 2):
    for inc in range(i, 4 * i + 1, i):
        if is_prime[curr_num + inc]:
            num_primes += 1
        total_nums += 1
    curr_num += 4 * i
    if num_primes / total_nums <= 0.1:
        print(i + 1)
        break