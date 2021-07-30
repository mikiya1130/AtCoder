N, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
minA = sumA / (4 * M)

A = sorted(A, reverse=True)

if A[M - 1] >= minA:
    print("Yes")
else:
    print("No")
