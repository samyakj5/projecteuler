triangle = []
square = []
pentagon = []
hexagon = []
heptagon = []
octagon = []

for i in range(1, 141):
    triangle.append(i * (i + 1) // 2)
    square.append(i**2)
    pentagon.append(i * (3 * i - 1))
    hexagon.append(i * (2 * i - 1))
    heptagon.append(i * (5 * i - 3) // 2)
    octagon.append(i * (3 * i - 2))

number_list = [heptagon, hexagon, pentagon, square, triangle]


# for oct in octagon:
#     if len(str(oct)) != 4 or str(oct)[2] == "0":
#         continue
#     print(oct)

for tri in triangle:
    if len(str(tri)) != 4 or str(tri)[2] == "0":
        continue
    print(tri)