N = int(input())

n = [[0] * 9 for _ in range(9)]
for i in range(1, N + 1):
    top = int(str(i)[0])
    bottom = int(str(i)[-1])

    if bottom != 0:
        n[top - 1][bottom - 1] += 1

ans = 0
for i in range(9):
    for j in range(9):
        ans += n[i][j] * n[j][i]

print(ans)
