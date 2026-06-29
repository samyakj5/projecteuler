pentagons = set()

for i in range(1, 10_000):
    pentagons.add(int(i * (3 * i - 1)/2))

sols = set()

for num1 in pentagons:
    for num2 in pentagons:
        if num1 + num2 in pentagons and abs(num1 - num2) in pentagons:
            sols.add(abs(num1 - num2))

print(min(sols))