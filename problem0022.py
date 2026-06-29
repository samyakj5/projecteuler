import math

with open("problem22_data.txt", "r", encoding="utf-8") as file:
    names_1 = file.read()
    
names = names_1.split(",")
names = [name.strip("\"").lower() for name in names]

names = sorted(names)

s = 0

for i in range(len(names)):
    score_list = [ord(c) - 96 for c in names[i]]
    score = sum(score_list) * (i + 1)
    s += score

print(s)