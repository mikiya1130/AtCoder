import itertools

N, M = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(N)]

if (B[0][0] - 1) % 7 > (B[0][0] + M - 2) % 7:
    print("No")
    exit()

for i, j in itertools.product(range(N), range(M)):
    if B[i][j] != B[0][0] + 7 * i + j:
        print("No")
        break
else:
    print("Yes")
