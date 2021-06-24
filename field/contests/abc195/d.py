import bisect

N, M, Q = map(int, input().split())
WV = []
for _ in range(N):
    WV.append(tuple(map(int, input().split())))
WV.sort(key=lambda x: x[1], reverse=True)

X = list(map(int, input().split()))

for i in range(Q):
    L, R = map(int, input().split())

    Xi = X.copy()
    del Xi[L-1:R]
    Xi.sort()

    value = 0
    for j, k in WV:
        idx = bisect.bisect_left(Xi, j)
        if idx < len(Xi):
            Xi.pop(idx)
            value += k

    print(value)
