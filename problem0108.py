import math

# n = 2**4 * 3**1 * 5**1

# sols = set()

# for x in range(n + 1, 2 * n + 1):
#     # if math.gcd(n, x) == 1:
#     #     continue
#     for y in range(x, n * x + 1):
#         # if math.gcd(n, x) == 1:
#         #     continue
#         if n * y + n * x == x * y:
#             sols.add((x, y))
#             break

# print(sorted(sols))
# print(len(sols))

# for i in range(len(primes)):
#     prime_lookups[math.prod(primes[0:i])] = primes[0:i]

# solutions = {}
# sum = 1

# for i in range(len(primes)):
#     sum += 3**i
#     solutions[math.prod(primes[0:i + 1])] = sum

# print(solutions)

# print(len(primes))

# ----------------------------------------------------------------

# If we have 1/x + 1/y = 1/n, we can turn this into yn + xn = xy => xy - yn - xn = 0
# Then, we apply SFFT to the eq. to get n^2 + xy - yn - xn = n^2 => (x - n)(y - n) = n^2
# We notice that, for (x, y) to be a solution, we can simply find all the divisors of n^2.
# If we find m divisors of n^2, then there are (m + 1)/2 solutions to the equation. So we must
# find n s.t. n^2 has 1999 divisors.

# Let n = prod(p_k^a_k) for p_k prime. Then n^2 = prod(p_k^(a_k)^2). To find the number of divisors of n^2,
# we use the formula m =  prod_k (2a_i - 1), since each prime can be included in 2a_i - 1 different ways each

# since we want the minimum value of n, we can find values a_k such that a_k <= a_(k + 1) (so that 2 has the largest exponent)

num_candidates = set()
MAX_DEGREE = 10
NUM_DIVISORS = 1_999

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