import math

triples = {}

for a in range(1, 1001):
    for b in range(a, 1001):
        if a + b > 1000:
            continue
        if a + b + math.sqrt(a**2 + b**2) <= 1000 and math.sqrt(a**2 + b**2) == int(math.sqrt(a**2 + b**2)):
            triples[a + b + int(math.sqrt(a**2 + b**2))] = triples.get(a + b + int(math.sqrt(a**2 + b**2)), 0) + 1

p = max(triples, key=triples.get)
print(p)

