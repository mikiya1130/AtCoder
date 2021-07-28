import itertools

N, M, Q = map(int, input().split())

L = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    L.append((a - 1, b - 1, c, d))

ans = 0
for A in itertools.combinations_with_replacement(range(1, M + 1), N):
    sum = 0
    for a, b, c, d in L:
        if A[b] - A[a] == c:
            sum += d
    ans = max(ans, sum)

print(ans)
