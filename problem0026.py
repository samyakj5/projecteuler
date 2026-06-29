import math

largest_num = 0

num_primes = 1000
is_prime = [False] + [False] + [True] * (num_primes - 2)

for i in range(math.ceil(math.sqrt(num_primes) + 1)):
    if is_prime[i]:
        for k in range(i**2, i, num_primes):
            is_prime[k] = False

for i in range(999, 10, -1):
    if is_prime[i]:
        for exp in range(1, i):
            if 10**exp % i == 1:
                if exp < i - 1:
                    break
                else:
                    largest_num = i
                    break
    if largest_num != 0:
        print(largest_num)
        break