import itertools

N = int(input())
XYH = [list(map(int, input().split())) for _ in range(N)]

CH = []
for Cx, Cy in itertools.product(range(101), repeat=2):
    H = None
    for x, y, h in XYH:
        if h == 0:
            continue
        tmp_h = h + abs(x - Cx) + abs(y - Cy)
        if H is None:
            H = tmp_h
            continue
        elif H == tmp_h:
            continue
        else:
            break
    else:
        CH.append(((Cx, Cy), H))

for (Cx, Cy), H in CH:
    for x, y, h in XYH:
        if h != max(H - abs(x - Cx) - abs(y - Cy), 0):
            break
    else:
        print(Cx, Cy, H)
