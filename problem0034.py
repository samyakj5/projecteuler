import math

s = 0

for i in range(10, 7 * math.factorial(9)):
    num = list(str(i))
    s_factorials = sum([math.factorial(int(digit)) for digit in num])

    if s_factorials == i:
        s += s_factorials

print(s)