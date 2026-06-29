with open("problem81_data.txt", "r", encoding="utf-8") as file:
    matrix = file.read()

matrix = [[int(x) for x in y.split(",")] for y in matrix.split("\n")]

MAT_SIZE = len(matrix)

for i in range(1, 2 * MAT_SIZE - 1):
    for j in range(0, i + 1):
        if 0 <= i - j < MAT_SIZE and 0 <= j < MAT_SIZE:
            if j != 0 and i - j != 0:
                matrix[i - j][j] += min(matrix[i - j - 1][j], matrix[i - j][j - 1])
            elif j == 0:
                matrix[i - j][j] += matrix[i - j - 1][j]
            elif i -j == 0:
                matrix[i - j][j] += matrix[i - j][j - 1]

print(matrix[-1][-1])