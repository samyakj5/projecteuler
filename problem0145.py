reversible = set()

odd_digits = {"1", "3", "5", "7", "9"}

for i in range(1_000_000_000):
    if str(i)[-1] == "0":
        continue
    reversed = str(i)[::-1]
    if set(str(int(reversed) + int(i))) <= odd_digits:
        reversible.add(i)
        reversible.add(int(reversed))

print(len(reversible))