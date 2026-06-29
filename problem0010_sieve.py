import math

num_primes = 2000000
is_prime = [True] * num_primes
is_prime[0] = False
is_prime[1] = False

for i in range(2, num_primes):
    if is_prime[i] == False:
        continue
    elif is_prime[i] == True:
        for k in range(2 * i, num_primes, i):
            is_prime[k] = False

list_primes = [x for x in range(num_primes) if is_prime[x]]
print(sum(list_primes))