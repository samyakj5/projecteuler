digit_fifths = set()

for i in range(10, 6 * 9**5):
    i_list = list(str(i))
    s = sum([int(x)**5 for x in i_list])
    if i == s:
        digit_fifths.add(i)

print(digit_fifths)
print(sum(digit_fifths))