import math

### tried dp, too slow

# UL = 100_000

# dp = [1] + [0] * UL

# for i in range(1, UL + 1):
#     if dp[i - 1] % 100 == 0:
#          print(i - 1)
#          print(dp[i - 1])
#          break
#     for c in range(i, UL + 1):
#         dp[c] += dp[c - i]


### pentagonal number theorem -> recurrence for calculating p(n)

UL = 100_000

pent = []

for i in range(1, UL + 1):
    pent.append(int(((i * (3 * i - 1) ) / 2)))
    pent.append(int(((-i * (3 * (-i) - 1)) / 2)))

partition = [1] + [0] * 2 * UL

for n in range(1, 2 * UL + 1):
    p_n = 0
    for k in range(1, len(pent) + 1):
        g_k = pent[k - 1]
        parity = math.ceil(k / 2)
        if n - g_k < 0:
            break
        p_n += (-1)**(parity - 1) * partition[n - g_k]
    partition[n] = p_n % 1_000_000

for i in range(0, len(partition)):
    if partition[i] == 0:
        print(i)
        break