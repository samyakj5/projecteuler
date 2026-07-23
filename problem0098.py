import math
from collections import Counter

with open("problem0098_data.txt", "r", encoding="utf-8") as file:
    words = file.read().replace("\"", "").split(",")

d = {}

for word in words:
    k = frozenset(Counter(word).items())
    if k in d:
        d[k].append(word)
    else:
        d[k] = [word]

c = frozenset(d.keys())

for k in c:
    if len(d[k]) == 1:
        d.pop(k)

cands = []
ma = 0

for g in d.values():
    m = len(g[0])
    if m > ma:
        ma = m
    cands.append(g)

sq = {_ : [] for _ in range(1, ma + 1)}

for x in range(1, math.isqrt(10**ma)):
    sq[len(str(x**2))].append(x**2)

largest = 0

for p in cands:
    l = len(p[0])
    y = sq[l]
    rep = l - len(set(p[0]))
    z = [q for q in y if (len(str(q)) - len(set(str(q))) == rep)]

    for num in z:
        i = str(num)
        di = {}
        v = True
        for d in range(l):
            c_dig = int(i[d])
            if c_dig in di and di[c_dig] != p[0][d]:
                v = False
                break
            elif c_dig in di:
                continue
            else:
                di[c_dig] = p[0][d]
        if v:
            n_di = {value: key for key, value in di.items()}
            n = ""
            for c in p[1]:
                n += str(n_di[c])
            if int(n) in sq[l]:
                if max(num, int(n)) > largest:
                    largest = max(num, int(n))

print(largest)