import math

def farey_generation(order):
    result = []
    
    x1 = 0
    y1 = 1
    x2 = 1
    y2 = order

    result.append((x1, y1))
    result.append((x2, y2))

    x = 0
    y = 0
    while y != 1:

        x = math.floor((y1 + order) / y2) * x2 - x1
        y = math.floor((y1 + order) / y2) * y2 - y1

        result.append((x, y))

        x1, x2, y1, y2 = x2, x, y2, y

    return result

result = farey_generation(12000)

count = -1

for numden in result:
    if numden == (1, 2):
        break
    if count != -1:
        count += 1
    if numden == (1, 3):
        count += 1

print(count)