W, H, N = map(int, input().split())
XYA = [list(map(int, input().split())) for _ in range(N)]

x0, y0 = 0, 0
x1, y1 = W, H
for x, y, a in XYA:
    if a == 1:
        x0 = max(x0, x)
    elif a == 2:
        x1 = min(x1, x)
    elif a == 3:
        y0 = max(y0, y)
    elif a == 4:
        y1 = min(y1, y)

print(max(0, x1 - x0) * max(0, y1 - y0))
