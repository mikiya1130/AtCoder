N, _ = map(int,input().split())
_, *A = map(int,input().split())
A = set(A)
for _ in range(N-1):
    _, *a = map(int,input().split())
    a = set(a)
    A &= a

print(len(A))
