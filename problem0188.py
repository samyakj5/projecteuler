import sys
import math
from sympy import totient

sys.set_int_max_str_digits(100_000)
sys.setrecursionlimit(10_000)

MOD = 100_000_000

def hyper(a, k):
    if k == 1:
        return a

    c = totient(MOD // (math.gcd(pow(a, math.ceil(math.log2(MOD))), MOD)))
    e = hyper(a, k - 1)
    return (pow(a, int((e % c) + c), MOD))

print(hyper(1777, 1855))
