import itertools

H, W = map(int, input().split())
S = [input() for _ in range(H)]


D = [["#"] * (W + 2) for _ in range(H + 2)]
for h, w in itertools.product(range(H), range(W)):
    if S[h][w] == ".":
        for hh in range(h, h + 3):
            D[hh][w : w + 3] = [".", ".", "."]

E = [["."] * (W + 2) for _ in range(H + 2)]
for h, w in itertools.product(range(1, H + 1), range(1, W + 1)):
    if D[h][w] == "#":
        for hh in range(h - 1, h + 2):
            E[hh][w - 1 : w + 2] = ["#", "#", "#"]

E = E[1:-1]
for i in range(H):
    E[i] = "".join(E[i][1:-1])

for s, e in zip(S, E):
    if s != e:
        print("impossible")
        break
else:
    print("possible")

    D = D[1:-1]
    for i in range(H):
        D[i] = "".join(D[i][1:-1])

    print(*D, sep="\n")
