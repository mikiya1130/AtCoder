import itertools

H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i, j in itertools.product(range(H), range(W)):
    if S[i][j] == ".":
        continue

    if i - 1 >= 0 and S[i - 1][j] == "#":
        continue
    elif i + 1 < H and S[i + 1][j] == "#":
        continue
    elif j - 1 >= 0 and S[i][j - 1] == "#":
        continue
    elif j + 1 < W and S[i][j + 1] == "#":
        continue

    print("No")
    break
else:
    print("Yes")
