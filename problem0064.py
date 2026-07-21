import math

UL = 10

for i in range(2, UL + 1):
    if math.sqrt(i) == math.isqrt(i):
        continue
    num = i - math.isqrt(i)
    while True:
        for j in range(1, 10):
            if num - 1 / j > 0:
                next = j - 1
                break
        