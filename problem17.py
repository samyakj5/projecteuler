tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

nums = []

for i in range(1, 1_000):
    if len(str(i)) == 1:
        nums.append(ones[i])
    elif len(str(i)) == 2:
        if i in teens:
            nums.append(teens[i])
        else:
            num = ""
            num += tens[int(str(i)[0])]
            if int(str(i)[1]) != 0:
                num +=  " " + ones[int(str(i)[1])]
            nums.append(num)
    elif len(str(i)) == 3:
        num = ""
        num += ones[int(str(i)[0])] + " hundred"
        j = int(str(i)[1:])
        if j != 0:
            if len(str(j)) == 1:
                num += " and " + ones[int(str(j)[0])]
            elif j in teens:
                num += " and " + teens[j]
            else:
                num += " and " + tens[int(str(j)[0])]
                if int(str(j)[1]) != 0:
                    num +=  " " + ones[int(str(j)[1])]
        nums.append(num)

nums.append("one thousand")

final = " ".join(nums)

print(len(final) - final.count(" "))