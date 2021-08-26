H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    S[i] = "." + S[i] + "."
S = ["." * (W + 2)] + S + ["." * (W + 2)]

for i in range(1, H + 1):
    ans = ""
    for j in range(1, W + 1):
        if S[i][j] == "#":
            ans += "#"
        else:
            cnt = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if S[i + ii][j + jj] == "#":
                        cnt += 1
            ans += str(cnt)
    print(ans)
