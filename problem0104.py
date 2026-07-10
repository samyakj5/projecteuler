import sys
sys.set_int_max_str_digits(100_000)

f1 = 1
f2 = 1
k = 2

while True:
    f1, f2 = f2, f1 + f2
    k += 1
    if len(str(f2)) >= 9:
        if len(set(str(f2)[:9])) == 9 and "0" not in str(f2)[:9]:
            if len(set(str(f2)[-9:])) == 9 and "0" not in str(f2)[-9:]:
                print(f2, k)
                break