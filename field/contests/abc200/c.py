from operator import mul
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

mod = {}
for a in A:
    a %= 200
    if a not in mod:
        mod[a] = 0
    mod[a % 200] += 1


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


count = 0
for n in mod.values():
    if n >= 2:
        count += cmb(n, 2)

print(count)
