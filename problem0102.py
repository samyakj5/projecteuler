import numpy as np

with open("problem0102_data.txt", "r", encoding="utf-8") as file:
    lines = file.read()

triangles = lines.split("\n")

count = 0

for triangle in triangles:
    coords = [int(i) for i in triangle.split(",", 5)]
    x1, y1, x2, y2, x3, y3 = coords

    z1 = x1 * y2 - x2 * y1
    z2 = x2 * y3 - x3 * y2
    z3 = x3 * y1 - x1 * y3

    if np.sign(z1) == np.sign(z2) == np.sign(z3):
        count += 1

print(count)