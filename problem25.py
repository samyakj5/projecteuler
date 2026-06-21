f1 = 1
f2 = 1

i = 2
while True:
    if len(str(f2)) == 1000:
        print(i)
        break
    f1, f2 = f2, f1 + f2
    i += 1