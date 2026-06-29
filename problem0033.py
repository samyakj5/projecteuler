import math

frac = set()

for i in range(10, 100):
    for j in range(10, i):

        frac1 = j /i

        num = str(j)
        den = str(i)

        print(num, den)

        for x in range(1, 10):
            if str(x) in num and str(x) in den:
                new_num = int(num.replace(str(x), "", 1))
                new_den = int(den.replace(str(x), "", 1))

                if new_den != 0:
                    frac2 = new_num / new_den

                    if frac1 == frac2:
                        frac.add((j, i))

num_prod = 1
den_prod = 1

for (num, den) in frac:
    num_prod *= num
    den_prod *= den

print(int(den_prod / math.gcd(num_prod, den_prod)))