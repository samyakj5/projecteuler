import math

num_candidates = set()
MAX_DEGREE = 10
NUM_DIVISORS = 7_999_999

num_primes = 50
is_prime = [False] * 2 + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

primes = [x for x in range(num_primes) if is_prime[x]]


def recurse_on_num(curr_num, curr_prime_idx, curr_degree, prev_degree, curr_divisors):
    if curr_prime_idx >= len(primes):
        return
    if curr_degree > MAX_DEGREE:
        return
    if curr_degree > prev_degree:
        return
    if curr_divisors >= NUM_DIVISORS:
        if not num_candidates:
            # print(curr_num, curr_prime_idx, curr_degree, prev_degree, curr_divisors)
            num_candidates.add(curr_num)
            return
        elif curr_num < min(num_candidates):
            # print(curr_num, curr_prime_idx, curr_degree, prev_degree, curr_divisors)
            num_candidates.add(curr_num)
            return
    
    curr_prime = primes[curr_prime_idx]
    ratio_num = (2 * (curr_degree + 1) + 1)
    ratio_den = (2 * curr_degree + 1)

    recurse_on_num(curr_num * curr_prime, curr_prime_idx, curr_degree + 1, prev_degree, (curr_divisors * ratio_num) // ratio_den)
    recurse_on_num(curr_num, curr_prime_idx + 1, 0, curr_degree, curr_divisors)

recurse_on_num(1, 0, 0, MAX_DEGREE, 1)

print(min(num_candidates))