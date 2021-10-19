xa, ya, xb, yb, xc, yc = map(int, input().split())

xa, ya, xb, yb, xc, yc = 0, 0, xb - xa, yb - ya, xc - xa, yc - ya
s = abs(xb * yc - yb * xc) / 2

print(s)
