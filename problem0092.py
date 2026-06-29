chains = {}
count_89 = 0

for i in range(1, 10_000_000):

    og_num = i

    while True:
        digs = list(str(i))
        i = sum([int(x)**2 for x in digs])
        if i == 89:
            count_89 += 1
            chains[og_num] = 89
            break
        elif i == 1:
            chains[og_num] = 1
            break
        elif i in chains:
            if chains[i] == 89:
                chains[og_num] = 89
                count_89 += 1
                break
            else:
                chains[og_num] = 1
                break

print(count_89)