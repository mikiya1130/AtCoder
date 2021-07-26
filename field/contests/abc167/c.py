N, M, X = map(int, input().split())

C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = 10 ** 7
for i in range(2 ** N):
    yen = 0
    exp = [0] * M

    for j in range(N):
        if (i >> j) & 1:
            yen += C[j]
            for k in range(M):
                exp[k] += A[j][k]

    if min(exp) >= X:
        ans = min(ans, yen)

if ans != 10 ** 7:
    print(ans)
else:
    print(-1)
