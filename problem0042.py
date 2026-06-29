with open("problem42_data.txt", "r", encoding="utf-8") as file:
    names_1 = file.read()

names = names_1.split(",")
names = [name.strip("\"").lower() for name in names]

triangle = set(x * (x + 1)/2 for x in range(1, 20))

count = 0

for i in range(len(names)):
    score_list = [ord(c) - 96 for c in names[i]]
    score = sum(score_list)
    if score in triangle:
        count += 1

print(count)