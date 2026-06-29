dec_str = "."

for i in range(1, 200000):
    dec_str += str(i)

prod = int(dec_str[1]) * int(dec_str[10]) * int(dec_str[100]) * int(dec_str[1_000]) * int(dec_str[10_000]) * int(dec_str[100_000]) * int(dec_str[1_000_000])

print(prod)