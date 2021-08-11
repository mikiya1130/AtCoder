N, M = map(int, input().split())
L = []
for i in range(M):
    P, Y = map(int, input().split())
    L.append([i, P, Y])

L = sorted(L, key=lambda x: (x[1], x[2]))

n = 1
p = 1
for i in range(M):
    _, P, Y = L[i]
    if p != P:
        p = P
        n = 1
    L[i][2] = n
    n += 1

L = sorted(L, key=lambda x: x[0])

for _, p, y in L:
    print("{:06}{:06}".format(p, y))
