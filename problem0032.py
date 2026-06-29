import math

pandigital = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

def factor(n):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    return factors

prods = set()

for i in range(1_000_000):
    if len(set(str(i))) < len(str(i)):
        continue

    for fact in factor(i):
            other = i // fact
            if len(set(str(fact))) == len(str(fact)) and len(set(str(other))) == len(str(other)):
                if len(set(str(i)) | set(str(fact)) | set(str(other))) == len(set(str(i))) + len(set(str(fact))) + len(set(str(other))):
                    if set(str(i)) | set(str(fact)) | set(str(other)) == pandigital:
                        prods.add(i)

print(sum(prods))