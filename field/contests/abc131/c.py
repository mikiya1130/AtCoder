import math


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return a * b // math.gcd(a, b)


A, B, C, D = map(int, input().split())
CD = lcm(C, D)

nC = B // C - (A + C - 1) // C + 1
nD = B // D - (A + D - 1) // D + 1
nCD = B // CD - (A + CD - 1) // CD + 1
n = B - A + 1

print(n - (nC + nD - nCD))
