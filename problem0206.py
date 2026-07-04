dig_array = ["1", "", "2", "", "3", "", "4", "", "5", "", "6","", "7", "", "8", "", "9", "", "0"]

cand_list = [x for x in range(1_200_000_000, 1_400_000_000) if x % 10 == 0]

print("here")

for i in cand_list:
    num = str(i**2)
    sol = True
    for j in range(0, len(str(num)), 2):
        if num[j] != dig_array[j]:
            sol = False
    if sol:
        print(i, i**2)
        break