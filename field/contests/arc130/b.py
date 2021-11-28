H, W, C, Q = map(int, input().split())
TNC = [list(map(int, input().split())) for _ in range(Q)]

Row = set()
Col = set()

cnt_r = 0
cnt_c = 0

Ans = [0] * C

for t, n, c in reversed(TNC):
    if t == 1:
        if n not in Row:
            Ans[c - 1] += W - cnt_c
            Row.add(n)
            cnt_r += 1
    else:
        if n not in Col:
            Ans[c - 1] += H - cnt_r
            Col.add(n)
            cnt_c += 1

print(*Ans)
