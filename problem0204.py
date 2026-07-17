import math

num_primes = 100
is_prime = bytearray(b"\x01") * num_primes
is_prime[0:2] = b"\x00\x00"

for k in range(4, num_primes, 2):
    is_prime[k] = 0

for i in range(3, math.isqrt(num_primes) + 1, 2):
    if is_prime[i]:
        for k in range(i*i, num_primes, 2*i):
            is_prime[k] = 0

primes = [x for x in range(num_primes) if is_prime[x]]

UL = 1_000_000_000
gen_hamming = {1}

def recurse_on_num(p_idx, curr_num):

    if curr_num > UL:
        return
    gen_hamming.add(curr_num)
    prime = primes[p_idx]
    recurse_on_num(p_idx, prime * curr_num)
    if p_idx - 1 >= 0:
        recurse_on_num(p_idx - 1, curr_num)

recurse_on_num(len(primes) - 1, 1)

print(len(gen_hamming))