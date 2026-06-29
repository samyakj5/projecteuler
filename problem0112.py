bouncy_nums = 0
total_nums = 0

curr = 1

while True:
    if total_nums:
        if bouncy_nums * 100 == total_nums * 99:
            break
    if sorted(str(curr)) == list(str(curr)):
        total_nums += 1
    elif sorted(str(curr))[::-1] == list(str(curr)):
        total_nums += 1
    else:
        bouncy_nums += 1
        total_nums += 1

    curr += 1

print(curr - 1)