import math


def lcm_list(list_n):
    x = list_n.pop(0)
    for i in range(len(list_n)):
        x = x * list_n[i] // math.gcd(x, list_n[i])
    return x


N = int(input())

A = list(map(int, input().split()))
m = lcm_list(A[:]) - 1
M = [m % a for a in A]

print(sum(M))
