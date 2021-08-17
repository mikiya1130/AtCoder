import collections

N = int(input())
S = [input() for _ in range(N)]
S = dict(collections.Counter(S))

M = int(input())
T = [input() for _ in range(M)]
for t in T:
    if t in S:
        S[t] -= 1

print(max(max(S.values()), 0))
