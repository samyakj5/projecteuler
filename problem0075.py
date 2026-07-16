from collections import Counter

def berggren(a, b, c, curr_d, max_d, trips):

    if (curr_d > max_d):
        return
    
    children = [
        (a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c),
        (a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c),
        (-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)
    ]
    for child in children:
        next_a, next_b, next_c = child
        if next_a + next_b + next_c <= 1_500_000:
            trips.append(child)
            berggren(next_a, next_b, next_c, curr_d + 1, max_d, trips)
        

trips = [(3, 4, 5)]
berggren(3, 4, 5, 0, 10_000, trips)

UL = 1_500_000

counts = [0] * (UL + 1)

for t in trips:
    p = sum(t)
    for k in range(p, UL + 1, p):
        counts[k] += 1

count = 0
for c in counts:
    if c == 1:
        count += 1

print(count)