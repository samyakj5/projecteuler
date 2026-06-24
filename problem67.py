with open("problem67_data.txt", "r", encoding="utf-8") as file:
    triangle = file.read()

rows = triangle.split('\n')

# just copied the code for problem 18 lol

row_nums = [x.split(' ') for x in rows]
row_nums = [[int(num) for num in row] for row in row_nums]

for row in range(len(rows) - 2, -1, -1):
    for num_idx in range(len(row_nums[row])):
        left = row_nums[row + 1][num_idx]
        right = row_nums[row + 1][num_idx + 1]
        row_nums[row][num_idx] += max(left, right)

print(row_nums[0][0])