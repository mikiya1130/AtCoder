from operator import mul
from functools import reduce
import collections


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
S = ["".join(sorted(input())) for _ in range(N)]
S = collections.Counter(S)

ans = 0
for n in S.values():
    if n >= 2:
        ans += cmb(n, 2)

print(ans)
