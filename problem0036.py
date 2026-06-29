def is_palindrome(num):
    return str(num) == str(num)[::-1]

s = 0

for i in range(1_000_000):
    if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
        s += i

print(s)
