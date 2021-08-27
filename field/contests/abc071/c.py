import collections

N = int(input())
A = list(map(int, input().split()))

A = collections.Counter(A)
A = [(i, n) for i, n in A.items() if n >= 2]
A = sorted(A, key=lambda x: x[0], reverse=True)

if len(A) >= 2:
    if A[0][1] >= 4:
        print(A[0][0] * A[0][0])
    else:
        print(A[0][0] * A[1][0])
else:
    print(0)
