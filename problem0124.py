import math

num_primes = 100_000
is_prime = [False] * 2 + [True] * (num_primes - 2)

for i in range(2, math.ceil(math.sqrt(num_primes)) + 1):
    if is_prime[i]:
        for k in range(i**2, num_primes, i):
            is_prime[k] = False

primes = [x for x in range(num_primes) if is_prime[x]]

for num in range(100_000, 1, -1):
    print(num)
    prime_factor_list = set()
    og_num = num
    while num > 1:
        found = False
        if num == 1:
            print(og_num)
            break
        for prime in primes:
            if num % prime == 0 and prime not in prime_factor_list:
                prime_factor_list.add(prime)
                num = num // prime
                found = True
        if not found:
            break
        

