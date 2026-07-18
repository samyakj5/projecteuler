from itertools import product
from collections import Counter

four_sided = [1, 2, 3, 4]
six_sided = [1, 2, 3, 4, 5, 6]

peter = list(product(four_sided, repeat=9))
colin = list(product(six_sided, repeat=6))

peter_sums = [sum(x) for x in peter]
colin_sums = [sum(x) for x in colin]

peter_counts = Counter(peter_sums)
colin_counts = Counter(colin_sums)

peter_total = sum(peter_counts.values())
colin_total = sum(colin_counts.values())

total = 0

for c in colin_counts:
    s = 0
    num = colin_counts[c]
    for p in peter_counts:
        if p > c:
            s += peter_counts[p] * num
    total += s

print(round(total / (peter_total * colin_total), 7))