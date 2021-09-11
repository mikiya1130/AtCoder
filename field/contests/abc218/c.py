import math

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

x, y = -1, -1
NS = []
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            if x == -1:
                NS += [(0, 0)]
                x, y = i, j
            else:
                NS += [(i - x, j - y)]

x, y = -1, -1
NT = []
for i in range(N):
    for j in range(N):
        if T[i][j] == "#":
            if x == -1:
                NT += [(0, 0)]
                x, y = i, j
            else:
                NT += [(i - x, j - y)]

LT = [[], [], [], []]
for rotate in range(4):
    for (tx, ty) in NT:
        x = round(
            math.cos(math.pi * rotate / 2) * tx - math.sin(math.pi * rotate / 2) * ty
        )
        y = round(
            math.sin(math.pi * rotate / 2) * tx + math.cos(math.pi * rotate / 2) * ty
        )
        LT[rotate] += [(x, y)]

for i in range(4):
    LT[i].sort()

SS = set(NS)
for lt in LT:
    ST = set()
    shift_x, shift_y = NS[0][0] - lt[0][0], NS[0][0] - lt[0][1]
    for x, y in lt:
        ST.add((x + shift_x, y + shift_y))

    if SS == ST:
        print("Yes")
        break
else:
    print("No")
