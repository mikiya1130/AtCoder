import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


a, b, n = [int(input()) for _ in range(3)]

l = lcm(a, b)
ans = l
while ans < n:
    ans += l

print(ans)
