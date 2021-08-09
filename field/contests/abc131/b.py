N, L = map(int, input().split())

A = [i for i in range(L, L + N)]

if 0 in A:
    print(sum(A))
elif A[0] > 0:
    print(sum(A[1:]))
else:
    print(sum(A[:-1]))
