from itertools import combinations
import math

T = 15
t = {x for x in range(2, T + 2)}

den = math.prod(t)
s = 1

for i in range(T // 2 + 1, T):
    bl = [set(x) for x in combinations(t, i)]
    for b in bl:
        r = t - b
        r_1 = {x - 1 for x in r}
        r_p = math.prod(r_1)
        s += r_p

print(math.floor(den / s))
