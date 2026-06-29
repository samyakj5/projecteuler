import math

perimeters = []

UL = 333_333_333

for i in range(2, UL):
    for add in (-1, 1):
        side = i + add
        a_sq_16 = (side)**2 * (4 * i**2 - (side)**2)
        a = math.isqrt(a_sq_16)
        if a * a == a_sq_16 and a % 4 == 0:
            perimeters.append(2 * i + side)

print(sum(perimeters))