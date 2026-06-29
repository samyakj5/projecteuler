multiples = set()
for i in range(1000):
    if i % 3 == 0:
        multiples.add(i)
    if i % 5 == 0:
        multiples.add(i)

print(sum(multiples))