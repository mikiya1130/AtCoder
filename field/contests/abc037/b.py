N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for _ in range(Q)]

A = [0] * N
for l, r, t in LRT:
    A[l - 1 : r] = [t] * (r - l + 1)

print(*A, sep='\n')
