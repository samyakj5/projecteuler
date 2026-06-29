chain_lengths = {}
longest_chain = 0
longest_chain_num = 0

def compute_collatz(num, chain_lengths):
    i = num
    chain_length = 1
    while True:
        if i == 1:                
            chain_lengths[num] = chain_length
            return chain_length
        elif i in chain_lengths:
            chain_length = chain_length + chain_lengths[i] - 1
            chain_lengths[num] = chain_length
            return chain_length
        
        elif i % 2 == 0:
            i = i // 2
            chain_length += 1
        else:
            i = 3 * i + 1
            chain_length += 1

for i in range(1, 1000000):
    chain_length = compute_collatz(i, chain_lengths)
    if chain_length > longest_chain:
        longest_chain = chain_length
        longest_chain_num = i

print(longest_chain_num, longest_chain)