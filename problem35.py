circs = set()

num_primes = 1_000_000
is_prime = [True] * num_primes

is_prime[0] = is_prime[1] = False

for i in range(2, num_primes):
    if is_prime[i] == True:
        for k in range(2 * i, num_primes, i):
            is_prime[k] = False

for i in range(num_primes):
    if not is_prime[i]:
        continue
    if is_prime[i]:
        is_circ = True
        for j in range(len(str(i))):
            c_prime = int(str(i)[j + 1:] + str(i)[:j + 1])
            # print(i, c_prime)
            if not is_prime[c_prime]:
                is_circ = False
                break
        
        if is_circ:
            circs.add(i)

print(len(circs))