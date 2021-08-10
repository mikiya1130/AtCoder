import math

N = int(input())
A = list(map(int, input().split()))

gl = [0] * N
gr = [0] * N
for i in range(1, N):
    gl[i] = math.gcd(gl[i - 1], A[i - 1])
    gr[N - i - 1] = math.gcd(gr[N - i], A[N - i])

ans = 0
for l, r in zip(gl, gr):
    ans = max(ans, math.gcd(l, r))

print(ans)
