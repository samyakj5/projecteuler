UL = 10_000

def is_palindrome(n):
    return str(n) == str(n)[::-1]

cycles = {}
lychrel = set()

for i in range(1, UL):
    og_num = i
    count = 0
    while True:
        if i in cycles:
            count += cycles[i]
            cycles[og_num] = count
            if count >= 50:
                lychrel.add(og_num)
                break
        i += int(str(i)[::-1])
        count += 1
        if is_palindrome(i):
            cycles[og_num] = count
            break
        if count >= 50:
            lychrel.add(og_num)
            break

print(len(lychrel))