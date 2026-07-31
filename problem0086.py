import math

UL = 100

def is_valid(a, b, c):
    return math.sqrt(a**2 + (b + c)**2).is_integer()

count = 0
found = []

for a in range(1, UL):
    for b in range(1, UL):
        for c in range(1, UL):
            if {a, b, c} in found:
                continue
            if is_valid(a, b, c) or is_valid(c, a, b) or is_valid(b, c, a):
                count += 1
                found.append({a, b, c})

print(count)