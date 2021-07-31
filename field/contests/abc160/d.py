import itertools
import collections

N, X, Y = map(int, input().split())
X -= 1
Y -= 1

dist = [[0] * (N - i - 1) for i in range(N - 1)]
for i, j in itertools.combinations(range(N), 2):
    d1 = j - i
    d2 = abs(X - i) + 1 + abs(Y - j)
    dist[i][j - i - 1] = min(d1, d2)

dist = itertools.chain.from_iterable(dist)
dist = collections.Counter(dist)

for i in range(1, N):
    if i in dist:
        print(dist[i])
    else:
        print(0)
