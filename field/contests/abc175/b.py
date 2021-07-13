import collections
import itertools

N = int(input())
L = list(map(int, input().split()))

L = collections.Counter(L)
L = sorted(L.items())

ans = 0
for (i, ni), (j, nj), (k, nk) in itertools.combinations(L, 3):
    if i + j > k:
        ans += ni * nj * nk

print(ans)
