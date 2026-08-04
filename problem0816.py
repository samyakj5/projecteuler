import math
import statistics

UL = 2_000_000

sn = 290797
sn1 = pow(sn, 2, 50515093)
s = [sn, sn1]

for i in range(1, 2 * UL):
    sn, sn1 = sn1, pow(sn1, 2, 50515093)
    s.append(sn1)

points = []

for i in range(UL):
    points.append((s[2 * i], s[2 * i + 1]))

points = sorted(points, key=lambda point: point[0])

def shortest_distance_brute(points):
    min = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.dist(points[i], points[j])
            if d < min:
                min = d

    return min

m = statistics.median([p[0] for p in points])


def shortest_distance(points, n):
    if n <= 100:
        return shortest_distance_brute(points)
    delta = min(shortest_distance(points[:n//2], len(points[1:n//2])), 
                shortest_distance(points[n//2:], len(points[n//2:])))
    
    C = [p for p in points if abs(p[0] - m) <= delta]
    C = sorted(C, key=lambda point: point[1])

    for i in range(1, len(C)):
        for j in range(i + 1, min(i + 10, len(C))):
            delta = min(math.dist(C[i], C[j]), delta)

    return delta

print(shortest_distance(points, len(points)))