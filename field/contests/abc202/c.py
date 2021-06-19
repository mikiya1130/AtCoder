import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [0] * N
for i in range(N):
    D[i] = B[C[i] - 1]

A = collections.Counter(A)
D = collections.Counter(D)
intersect = A.keys() & D.keys()

count = 0
for i in intersect:
    count += A[i] * D[i]

print(count)
