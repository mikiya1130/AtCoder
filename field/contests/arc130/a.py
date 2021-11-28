from operator import mul
from functools import reduce
from functools import lru_cache


@lru_cache()
def cmb(n, r):
    if n >= r >= 0:
        r = min(n - r, r)
        if r == 0:
            return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under
    else:
        return 0


N = int(input())
S = input() + "A"

ans = 0
pre = ""
cnt = 0
for s in S:
    if pre == s:
        cnt += 1
    else:
        ans += cmb(cnt, 2)
        cnt = 1
    pre = s

print(ans)
