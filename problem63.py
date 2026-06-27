count = 0

for i in range(1, 10):
    for j in range(1, 22):
        if j == len(str(i**j)):
            count += 1

print(count)