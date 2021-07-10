N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N, 2):
    A[i] -= 1

s = sum(A)

if s <= X:
    print('Yes')
else:
    print('No')
