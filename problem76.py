num_list = [1] + [0] * 100

for n in range(1, 101):
    for s in range(n, 101):
        num_list[s] += num_list[s - n]

print([num_ways - 1 for num_ways in num_list][100])