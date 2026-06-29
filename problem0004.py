def is_palindrome(num):
    return str(num) == str(num)[::-1]

largest = 0

for i in range(999, 99, -1):
    if i * i < largest:
        break
    for j in range(i, 99, -1):
        if is_palindrome(i * j) and (i * j) > largest:
            largest = i * j

print(largest)