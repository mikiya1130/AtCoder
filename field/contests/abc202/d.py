from operator import mul
from functools import reduce

A, B, K = map(int, input().split())
N = A + B


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


ans = ''
for _ in range(N):
    if A >= 1:
        sum = cmb(A-1+B, B)
        if K <= sum:
            ans += 'a'
            A -= 1
        else:
            K -= sum
            ans += 'b'
            B -= 1
    else:
        ans += 'b'
        B -= 1

print(ans)
