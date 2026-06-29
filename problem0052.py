from collections import Counter

for i in range(1, 1_000_000):
    digs = Counter(str(i))
    mult = True
    for j in range(2, 7):
        if digs != Counter(str(j * i)):
            mult = False
    if mult:
        print(i)
        break