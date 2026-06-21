num_primes = 1_000_000
is_prime = [True] * num_primes
is_prime[0] = False
is_prime[1] = False

for i in range(2, num_primes):
    if is_prime[i] == False:
        continue
    else:
        for k in range(2 * i, num_primes, i):
            is_prime[k] = False

largest_cons_prime = 2
largest_cons = 0

for j in range(int(num_primes/2)):
    p_count = 0
    sum = 0
    for i in range(j, num_primes):
        if is_prime[i]:
            p_count += 1
            sum += i
            if sum >= num_primes:
                break
            if is_prime[sum] and p_count > largest_cons:
                largest_cons = p_count
                largest_cons_prime = sum


print(largest_cons_prime)