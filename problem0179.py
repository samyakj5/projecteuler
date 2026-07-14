import math
from sympy import factorint

# def factor(n):
#     factors = set()
#     for i in range(1, math.ceil(math.sqrt(n)) + 1):
#         if n % i == 0:
#             factors.add(n // i)
#             factors.add(i)

#     return factors

UL = 10_000_000
num_factor_counts = [0, 0, 2]
c = 0

for n in range(3, UL):
    factors = factorint(n)
    prod_list = [x + 1 for x in factors.values()]
    count = math.prod(prod_list)
    num_factor_counts.append(count)
    if num_factor_counts[n - 1] == count:
        c += 1

print(c)