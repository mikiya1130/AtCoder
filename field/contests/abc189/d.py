from functools import lru_cache
import sys
sys.setrecursionlimit(10000000)

N = int(input())

S = []
for i in range(N):
    S.append(True if input() == 'AND' else False)


@lru_cache(maxsize=None)
def dfs(i, yi):
    if i == 0:
        return 1

    if yi:
        if S[i-1]:
            return dfs(i-1, True)
        else:
            return dfs(i-1, True) * 2 + dfs(i-1, False)
    else:
        if S[i-1]:
            return dfs(i-1, True) + dfs(i-1, False) * 2
        else:
            return dfs(i-1, False)


print(dfs(N, True))
