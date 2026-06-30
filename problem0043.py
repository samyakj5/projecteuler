candidates = [f"{i:03d}" for i in range(17, 1000, 17) if len(str(i)) == len(set(str(i))) and len(str(i)) >= 2]

nums = [13, 11, 7, 5, 3, 2, 1]

for num in nums:
    num
    new_cands = []
    for candidate in candidates:
        last_2_digs = candidate[0:2]
        remaining_digs = {str(i) for i in range(0, 10)} - set(candidate)
        for first_dig in remaining_digs:
            if int(first_dig + last_2_digs) % num == 0:
                new_cands.append(first_dig + candidate)
    
    candidates = new_cands

print(sum([int(candidate) for candidate in candidates]))