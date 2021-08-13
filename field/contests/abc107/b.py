def transpose(A, w):
    tA = []
    for i in range(w):
        col = [a[i] for a in A]
        tA.append("".join(col))

    return tA


H, W = map(int, input().split())
A = [input() for _ in range(H)]

A = [row for row in A if row != "." * W]
tA = transpose(A, W)
tW = len(tA[0])
tA = [row for row in tA if row != "." * tW]
A = transpose(tA, tW)

for a in A:
    print(a)
