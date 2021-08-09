H, W = map(int, input().split())
S = [input() for _ in range(H)]

nW = [[] for _ in range(H)]
for h in range(H):
    pre = 0
    n = 0
    for w in range(W):
        if S[h][w] == "#":
            nW[h].extend([n] * n)
            nW[h].append(0)
            n = 0
        else:
            n += 1
    nW[h].extend([n] * n)

nH = [[] for _ in range(H)]
for w in range(W):
    pre = 0
    n = 0
    for h in range(H):
        if S[h][w] == "#":
            for i in range(1, n + 1):
                nH[h - i].append(n)
            nH[h].append(0)
            n = 0
        else:
            n += 1
    for i in range(0, n):
        nH[h - i].append(n)

ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, nW[h][w] + nH[h][w] - 1)

print(ans)
