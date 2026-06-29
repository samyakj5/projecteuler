import math
from decimal import Decimal, getcontext

getcontext().prec = 102

# xk_list = ["0", ".", "7"]
# x_k = x_0 = Decimal(0.7)

# for i in range(1, 10):
#     x_k1 = (x_k + 2 / x_k) / 2
#     x_k = x_k1

# print(x_k1)
# print(len(str(x_k1)))

# x = [int(x) for x in str(x_k1) if x != "."]
# print(sum(x))

sum_digs = 0

for i in range(0, 101):
    if len(str(math.sqrt(i))) <= 5:
        continue

    xk_list = list(str(math.sqrt(i)))
    x_k = x_0 = Decimal(math.sqrt(i))

    for j in range(1, 11):
        x_k1 = (x_k + i / x_k) / 2
        x_k = x_k1

    for d in range(0, 101):
        if str(x_k1)[d] == ".":
            continue
        sum_digs += int(str(x_k1)[d])

print(sum_digs)

