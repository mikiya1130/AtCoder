N, x = map(int, input().split())
A = list(map(int, input().split()))

A = [0] + A + [0]
B = [A[i] + A[i + 1] - x for i in range(N + 1)]

ans = 0
for i in range(N):
    if B[i] > 0:
        ans += B[i]
        B[i + 1] -= B[i]
if B[-1] > 0:
    ans += B[-1]

print(ans)
