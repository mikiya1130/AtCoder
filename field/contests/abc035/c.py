import itertools

N, Q = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(Q)]

A = [0] * N

for l, r in LR:
    A[l - 1] += 1
    if r < N:
        A[r] -= 1

A = tuple(itertools.accumulate(A))

for a in A:
    print(a % 2, end="")
print()
