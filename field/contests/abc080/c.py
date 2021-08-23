N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = None
for i in range(1, 2 ** 10):
    s = 0
    for j in range(N):
        n = 0
        for k in range(10):
            n += F[j][k] * (i >> k & 1)
        s += P[j][n]
    if ans is None:
        ans = s
    else:
        ans = max(ans, s)

print(ans)
