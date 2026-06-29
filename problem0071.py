import math

min = 0
max = 3/7

num, den = 0, 0

for d in range(1, 1_000_000):
    for n in range(math.floor(3/7 * d - 1), math.ceil(3/7 * d + 1)):
        if min < n/d < max:
            min = n/d
            num, den = n, d

print(num, den)