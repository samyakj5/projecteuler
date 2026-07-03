with open("problem0059_data.txt", "r", encoding="utf-8") as file:
    data = file.read().split(",")

# for a in range(ord('a'), ord('z') + 1):
#     for b in range(ord('a'), ord('z') + 1):
#         for c in range(ord('a'), ord('z') + 1):
#             cipher = [a, b, c]
#             result = ""
#             for i in range(len(data)):
#                 result += chr(cipher[i % 3] ^ int(data[i]))
#             if "the" in result and "|" not in result:
#                 print(result, a, b, c)


# Cipher found from above: 101, 120, 112

cipher = [101, 120, 112]

result = ""

for i in range(len(data)):
    result += chr(cipher[i % 3] ^ int(data[i]))

sum = 0

for ch in result:
    sum += ord(ch)

print(sum)

