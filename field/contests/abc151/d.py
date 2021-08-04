H, W = map(int, input().split())

S = []
for _ in range(H):
    S.append(input())

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue

        E = [[None] * W for _ in range(H)]

        E[i][j] = 0
        V = [(i, j)]
        for ii, jj in V:
            if ii - 1 >= 0 and S[ii - 1][jj] == "." and E[ii - 1][jj] is None:
                E[ii - 1][jj] = E[ii][jj] + 1
                V.append((ii - 1, jj))
            if ii + 1 < H and S[ii + 1][jj] == "." and E[ii + 1][jj] is None:
                E[ii + 1][jj] = E[ii][jj] + 1
                V.append((ii + 1, jj))
            if jj - 1 >= 0 and S[ii][jj - 1] == "." and E[ii][jj - 1] is None:
                E[ii][jj - 1] = E[ii][jj] + 1
                V.append((ii, jj - 1))
            if jj + 1 < W and S[ii][jj + 1] == "." and E[ii][jj + 1] is None:
                E[ii][jj + 1] = E[ii][jj] + 1
                V.append((ii, jj + 1))

        for e in E:
            for ee in e:
                if ee is not None:
                    ans = max(ans, ee)

print(ans)
