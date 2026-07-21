from collections import Counter

UL = 10_000_000

phi = [i for i in range(UL)]

for i in range(2, UL):
    if phi[i] == i:
        for k in range(i, UL, i):
            phi[k] -= (phi[k] // i)

min_ratio = float('inf')
min_n = 2

for i in range(2, UL):
    if Counter(str(i)) == Counter(str(phi[i])):
        if i / phi[i] < min_ratio:
            min_ratio = i / phi[i]
            min_n = i

print(min_n)