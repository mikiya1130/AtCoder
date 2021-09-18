import itertools

A = [list(map(int, input().split())) for _ in range(4)]

V = set()
for i, j in itertools.product(range(4), repeat=2):
    if A[i][j] == 1:
        V.add((i, j))

ans = 0
for i in range(2 ** 16):
    B = set()
    for n in range(16):
        if i >> n & 1:
            B.add(n)

    if B < V:
        continue

    for i in range(4):
        C = B & set(range(4 * i, 4 * (i + 1)))
        print(C)


print(ans)
