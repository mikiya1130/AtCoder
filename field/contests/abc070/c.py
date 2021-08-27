import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


def lcm_list(list_n):
    x = list_n.pop(0)
    for i in range(len(list_n)):
        x = x * list_n[i] // math.gcd(x, list_n[i])
    return x


N = int(input())
T = [int(input()) for _ in range(N)]

print(lcm_list(T))
