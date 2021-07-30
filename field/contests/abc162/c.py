import math
import itertools


def gcd_list(list_n):
    x = list_n.pop(0)
    for i in range(len(list_n)):
        x = math.gcd(x, list_n[i])
    return x


K = int(input())

ans = 0
for a, b, c in itertools.combinations(range(1, K + 1), 3):
    ans += gcd_list([a, b, c]) * 6

for a, b in itertools.combinations(range(1, K + 1), 2):
    ans += math.gcd(a, b) * 6

for a in range(1, K + 1):
    ans += a

print(ans)
