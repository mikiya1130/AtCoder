N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

BC = [list(map(int, input().split())) for _ in range(M)]
BC = sorted(BC, key=lambda x: x[1], reverse=True)
D = []
idx = 0
for b, c in BC:
    D.extend([c] * b)
    idx += b
    if idx >= N:
        break
if idx < N:
    D.extend([0] * (N - idx))

ans = 0
for a, d in zip(A, D[:N]):
    ans += max(a, d)

print(ans)
