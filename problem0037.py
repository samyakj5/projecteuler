truncatable = set()

num_primes = 10_000_00
is_prime = [True] * num_primes

is_prime[0] = False
is_prime[1] = False

for i in range(num_primes):
    if is_prime[i] == False:
        continue
    
    else:
        for j in range(2 * i, num_primes, i):
            is_prime[j] = False

        # check if truncatable
        if len(str(i)) > 1:
            n1 = str(i)
            n2 = str(i)

            trunc = True

            while len(n1) > 1:
                n1 = n1[1:]
                n2 = n2[:-1]
                if is_prime[int(n1)] and is_prime[int(n2)]:
                    continue
                else:
                    trunc = False
                    break

            if trunc:
                truncatable.add(i)

print(truncatable)
print(sum(truncatable))

