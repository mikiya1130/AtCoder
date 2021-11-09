import itertools
from functools import lru_cache
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
P = [int(input()) for _ in range(Q)]


@lru_cache(maxsize=700000)
def delicious(x, y, w, h):
    if w == 0 and h == 0:
        return D[x][y]
    elif w == 0:
        return delicious(x, y, w, h - 1) + D[x + w][y + h]
    elif h == 0:
        return delicious(x, y, w - 1, h) + D[x + w][y + h]
    else:
        return (
            delicious(x, y, w, h - 1)
            + delicious(x, y, w - 1, h)
            - delicious(x, y, w - 1, h - 1)
            + D[x + w][y + h]
        )


MAX_D = [0] * (N * N + 1)
for x, y in itertools.product(range(N), repeat=2):
    for w in range(N - x):
        for h in range(N - y):
            size = (w + 1) * (h + 1)
            d = delicious(x, y, w, h)
            if MAX_D[size] < d:
                MAX_D[size] = d

max_d = MAX_D[0]
for i in range(len(MAX_D)):
    if MAX_D[i] < max_d:
        MAX_D[i] = max_d
    else:
        max_d = MAX_D[i]

for p in P:
    print(MAX_D[p])
