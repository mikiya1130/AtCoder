import math


def gcd(a, b):
    return math.gcd(a, b)


def gcd_list(list_n):
    x = list_n.pop(0)
    for i in range(len(list_n)):
        x = math.gcd(x, list_n[i])
    return x


N, *X = map(int, input().split())
X += list(map(int, input().split()))

X.sort()

diff = []
for i in range(N):
    diff.append(X[i + 1] - X[i])

print(gcd_list(diff))
