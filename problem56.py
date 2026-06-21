nums = set()

def digital_sum(num):
    num = list(str(num))
    num = [int(i) for i in num]
    return sum(num)

for a in range(1, 100):
    for b in range(1, 100):
        nums.add(a**b)

digital_sums = set()

for num in nums:
    digital_sums.add(digital_sum(num))

print(max(digital_sums))