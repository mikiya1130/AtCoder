N = int(input())
A = [int(input()) for _ in range(N)]

maxA = max(A)
idx = A.index(maxA)
A.pop(idx)
maxA2 = max(A)

for i in range(N):
    if i != idx:
        print(maxA)
    else:
        print(maxA2)
