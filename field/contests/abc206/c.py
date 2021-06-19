import collections
from operator import mul
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += i


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


A = collections.Counter(A)
count = 0
for v in A.values():
    if v >= 2:
        count += cmb(v, 2)

print(sum - count)
