import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 6)

S = int(input())


@lru_cache(maxsize=None)
def dp(s):
    if s == 1 or s == 2:
        return 0
    elif s == 3:
        return 1

    return dp(s - 1) + dp(s - 3)


print(dp(S) % (10 ** 9 + 7))
