import math

# # brute force

# increasing_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# decreasing_nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# MAX_DIGS = 11

# increasing = set()
# decreasing = set()

# def find_increasing_nums(curr_idx, curr_num):
#     if curr_num != 0:
#         if int(math.log10(curr_num)) + 1 > MAX_DIGS:
#             return
#     increasing.add(curr_num)
#     find_increasing_nums(curr_idx, curr_num * 10 + increasing_nums[curr_idx])
#     if curr_idx + 1 < len(increasing_nums):
#         find_increasing_nums(curr_idx + 1, curr_num)

# def find_decreasing_nums(curr_idx, curr_num):
#     if curr_num != 0:
#         if int(math.log10(curr_num)) + 1 > MAX_DIGS:
#             return
#     # if curr_num == 0 and 0 in decreasing:
#     #     return
#     decreasing.add(curr_num)
#     find_decreasing_nums(curr_idx, curr_num * 10 + decreasing_nums[curr_idx])
#     if curr_idx + 1 < len(decreasing_nums) and not (curr_num == 0 and decreasing_nums[curr_idx + 1] == 0):
#         find_decreasing_nums(curr_idx + 1, curr_num)

# find_increasing_nums(0, 0)
# find_decreasing_nums(0, 0)

# print(len(increasing) - 1)
# print(len(decreasing) - 1)

# dp?

MAX_DIGS = 100

# increasing nums

inc_curr_vals = [1] * 9
inc_final_vals = [1] * 9

for level in range(MAX_DIGS - 1):
    inc_next_vals = [0] * 9
    for i in range(len(inc_curr_vals)):
        for j in range(i + 1):
            inc_next_vals[j] += inc_curr_vals[i]
    inc_curr_vals = inc_next_vals
    for i in range(len(inc_curr_vals)):
        inc_final_vals[i] += inc_curr_vals[i]

inc = sum(inc_final_vals)

# decreasing nums

dec_curr_vals = [0] + [1] * 9
dec_final_vals = [0] + [1] * 9

for level in range(MAX_DIGS - 1):
    dec_next_vals = [0] * 10
    for i in range(len(dec_curr_vals)):
        for j in range(i + 1):
            dec_next_vals[j] += dec_curr_vals[i]
    dec_curr_vals = dec_next_vals
    for i in range(len(dec_curr_vals)):
        dec_final_vals[i] += dec_curr_vals[i]

dec = sum(dec_final_vals)

# neutral nums

neutral = 9 * MAX_DIGS

total = inc + dec - neutral

print(total)