N = int(input())
A = list(map(int, input().split()))

A.sort()

B = set()
for i in range(N):
    if i >= 1 and A[i - 1] == A[i]:
        B.add(A[i])
        continue
    for a in range(A[i] * 2, A[-1] + 1, A[i]):
        B.add(a)

setA = set(A)
print(len(setA) - len(setA & B))
