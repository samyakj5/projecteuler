import math

with open("problem99_data.txt", "r", encoding="utf-8") as file:
    lines = file.read().split("\n")

largest_log = 0
largest_line = 0
line_num = 0

for line in lines:
    line_num += 1
    nums = line.split(",")
    val = int(nums[1]) * math.log10(int(nums[0]))
    if val > largest_log:
        largest_log = val
        largest_line = line_num

print(largest_line, largest_log)