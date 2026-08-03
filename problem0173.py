import math

UL = 1_000_000

# # brute force

# count = 0

# for i in range(2, UL + 1, 2):
#     for j in range(i - 2, 0, -2):
#         if i**2 - j**2 <= UL:
#             count += 1

# for i in range(3, UL + 1, 2):
#     for j in range(i - 2, 0, -2):
#         if i**2 - j**2 <= UL:
#             count += 1

# print(count)

e = [4]
e_sum = 0
o = [1]
o_sum = 0

for i in range(3, UL):
    if i % 2 == 0:
        e_sum += i**2 - (i - 2)**2
        e.append(e_sum)
        if e_sum - e[len(e) - 2] > UL:
            break
    else:
        o_sum += i**2 - (i - 2)**2
        o.append(o_sum)
        if o_sum - o[len(o) - 2] > UL:
            break

count = 0

I = 0
O = 1

while I <= O:
    # print(I, O, count)
    if O + 1 < len(e):
        d = e[O + 1] - e[I]
        if UL - d >= 0:
            O += 1
            continue
    count += O - I
    I += 1

I = 0
O = 1

while I <= O:
    if O + 1 < len(o):
        d = o[O + 1] - o[I]
        if UL - d >= 0:
            O += 1
            continue
    count += O - I
    I += 1

print(count)