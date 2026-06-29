import math

chains = {}

chains[145] = 1
chains[40585] = 1
chains[169] = chains[363601] = chains[1454] = 3
chains[871] = chains[45361] = chains[872] = chains[45362] = 2
chains[1] = 1
chains[2] = 1

for i in range(3, 1_000_000):
    if i in chains:
        continue
    og_num = i
    curr_chain = 0
    while True:
        digs = list(str(i))
        if i in chains:
            curr_chain += chains[i]
            chains[og_num] = curr_chain
            break
        else:
            curr_chain += 1
        i = sum([math.factorial(int(d)) for d in digs])


chain_60 = 0

for c in chains.values():
    if c == 60: chain_60 += 1

print(chain_60)


