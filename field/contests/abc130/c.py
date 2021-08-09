W, H, x, y = map(int, input().split())

if W % 2 == 0:
    Cx = W // 2
else:
    Cx = W / 2

if H % 2 == 0:
    Cy = H // 2
else:
    Cy = H / 2

if Cx == x and Cy == y:
    div = 1
else:
    div = 0
s = W * H / 2

print(s, div)
