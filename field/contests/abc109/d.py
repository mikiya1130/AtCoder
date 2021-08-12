H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

move = []
for i in range(H):
    for j in range(W - 1):
        if A[i][j] % 2 == 1:
            A[i][j] -= 1
            A[i][j + 1] += 1
            move.append((i + 1, j + 1, i + 1, j + 2))

for i in range(H - 1):
    if A[i][-1] % 2 == 1:
        A[i][-1] -= 1
        A[i + 1][-1] += 1
        move.append((i + 1, W, i + 2, W))

print(len(move))
for m in move:
    print(*m)
