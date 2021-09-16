from operator import mul
from functools import reduce

N = int(input())
A = map(int, input().split())

B = []
i = 0
prev = 0
for a in A:
    if a > prev:
        i += 1
    else:
        B.append(i)
        i = 1
    prev = a
B.append(i)


def cmb(n, r):
    assert n >= r >= 0

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


ans = 0
for b in B:
    if b == 1:
        ans += 1
    else:
        ans += cmb(b, 2) + b

print(ans)
