N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

A = [set() for _ in range(N)]

for x, y in XY:
    A[x - 1].add(y - 1)
    A[y - 1].add(x - 1)

ans = 1
for i in range(1, 2 ** N):
    S = set()
    for j in range(N):
        if i >> j & 1:
            S.add(j)

    for s in S:
        if (S - set([s])).issubset(A[s]):
            continue
        else:
            break
    else:
        ans = max(ans, len(S))

print(ans)
