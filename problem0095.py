UL = 1_000_000

chains = {}

def get_divisors(n):
    if n <= 1:
        return []

    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)

            if i != n // i:
                divisors.append(n // i)

    return divisors

chains = {}

for i in range(2, UL):

    chain = [i]

    og = i
    i = sum(get_divisors(i))

    while True:

        chain.append(i)

        if i > UL:
            break

        if i == 1:
            chains[og] = chain
            break

        if i == og:
            chains[og] = chain
            break

        if i in chains:
            chains[og] = chain + chains[i]
            break

        if i in chain[:-1]:
            break
        
        i = sum(get_divisors(i))

        

l = [x for x, y in chains.items() if x == y[-1]]

max = 0
smallest = float('inf')

for z in l:
    if len(chains[z]) > max:
        max = len(chains[z])
        smallest = min(chains[z])

print(smallest)