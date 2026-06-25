import math

def factor(n):
    factors = set()
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    factors.add(1)
    return factors

def is_abundant(n):
    if n < 12:
        return False
    return (sum(factor(n)) > n)

abundant_nums = set()

for i in range(1, 28124):
    if is_abundant(i):
        abundant_nums.add(i)

abundant_nums

abundant_nums_sum = set()

for num1 in abundant_nums:
    for num2 in abundant_nums:
        abundant_nums_sum.add(num1 + num2)


natural_nums = {i for i in range(1, 28124)}

print(sum(natural_nums - abundant_nums_sum))