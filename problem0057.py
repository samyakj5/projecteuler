count = 0
    
prev_prev_den = 1
prev_den = 2
curr_den = 5

for i in range(1, 999):
    prev_prev_den, prev_den = prev_den, curr_den
    curr_den = 2 * prev_den + prev_prev_den
    if len(str(curr_den + prev_den)) > len(str(curr_den)):
        count += 1

print(count)