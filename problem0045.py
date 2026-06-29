triangles = set()
for t in range(1_000_000):
    triangles.add(t * (t + 1) / 2)

pentagons = set()
for p in range(1_000_000):
    pentagons.add(p * (3 * p - 1) / 2)

hexagons = set()
for h in range(1_000_000):
    hexagons.add(h * (2 * h - 1))

print(triangles.intersection(pentagons).intersection(hexagons))