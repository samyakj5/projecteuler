import math

def calc_sum(n):
    return sum(list(range(1, n + 1)))

lowest_diff = math.inf
area = 0

UL = 100

for num1 in range(UL):
    for num2 in range(UL):
        if abs(2_000_000 - calc_sum(num1) * calc_sum(num2)) < lowest_diff:
            area = num1 * num2
            lowest_diff = abs(2_000_000 - calc_sum(num1) * calc_sum(num2))

print(area)