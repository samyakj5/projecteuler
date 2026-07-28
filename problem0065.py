UL = 100

c = [1 for _ in range(UL)]

for i in range(1, UL // 3 + 1):
    c[3 * i - 1] = 2 * i

c[0] += 1

c = c[::-1]

def recurse_find(c_num, c_den, idx):
    if idx >= len(c):
        return c_den, c_num
    c_num, c_den = c_den, c[idx] * c_den + c_num
    return recurse_find(c_num, c_den, idx + 1)

i_num = 1
i_den = c[0]
idx = 1


num, den = recurse_find(i_num, i_den, idx)

print(sum(map(int, str(num))))