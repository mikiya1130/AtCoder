import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


N = int(input())
print(lcm(2, N))
