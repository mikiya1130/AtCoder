import collections

N = int(input())
A = list(map(int, input().split()))
A = collections.Counter(A)

for i in range(1, N + 1):
    if i in A:
        print(A[i])
    else:
        print(0)
