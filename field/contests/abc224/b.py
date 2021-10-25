import itertools

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

bl = True
for i1, i2 in itertools.combinations(range(H), 2):
    for j1, j2 in itertools.combinations(range(W), 2):
        if A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]:
            continue
        bl = False

if bl:
    print("Yes")
else:
    print("No")
