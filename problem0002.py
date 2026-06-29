
f1 = 1
f2 = 2

even_fib = set()

while True:
    if f1 % 2 == 0:
        even_fib.add(f1)
    if f2 > 4000000:
        print(sum(even_fib))
        break
    f1, f2 = f2, f1 + f2
    