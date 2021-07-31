import collections
from operator import mul
from functools import reduce
from functools import lru_cache


@lru_cache(maxsize=None)
def cmb(n, r):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))
cntA = collections.Counter(A)
cmbA = {k: cmb(v, 2) for k, v in cntA.items()}
sumCmbA = sum(cmbA.values())

for i in range(N):
    ans = sumCmbA
    if A[i] in cmbA:
        ans -= cmbA[A[i]]
        ans += cmb(cntA[A[i]] - 1, 2)
    print(ans)
