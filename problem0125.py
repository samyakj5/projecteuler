import math

UL = 100_000_000

palindromes = []
palindromic_sums = []

for num in range(2, UL):
    if str(num) == str(num)[::-1]:
        palindromes.append(num)

for palindrome in palindromes:
    first = 1
    last = 2
    s = 1**2 + 2**2
    while first < last:
        if s < palindrome:
            last += 1
            s += last**2
        elif s > palindrome:
            s -= first**2
            first += 1
        elif s == palindrome:
            palindromic_sums.append(palindrome)
            break

print(sum(palindromic_sums))