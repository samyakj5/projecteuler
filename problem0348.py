import math

nums = {}

UL = 1_000_000_000

for n1 in range(2, math.isqrt(UL)):
    for n2 in range(2, int(math.cbrt(UL))):
        n = pow(n1, 2) + pow(n2, 3)
        nums[n] = nums.get(n, 0) + 1

x = [n[0] for n in nums.items() if n[1] == 4]
x.sort()

r = []

for i in x:
    if str(i) == str(i)[::-1]:
        r.append(i)

print(sum(r[:5]))