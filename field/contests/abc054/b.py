import itertools

N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for i, j in itertools.product(range(N - M + 1), repeat=2):
    for ii, jj in itertools.product(range(M), repeat=2):
        if A[i + ii][j + jj] != B[ii][jj]:
            break
    else:
        print("Yes")
        break
else:
    print("No")
