sum = 1
curr = 1

for i in range(2, 1001, 2):
    sum += 4 * curr + 10 * i
    curr += 4 * i

print(sum)