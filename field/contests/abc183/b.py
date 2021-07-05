Sx, Sy, Gx, Gy = map(int, input().split())

Sy = -Sy
if Gx == Sx:
    print(Sx)
else:
    a = (Gy - Sy) / (Gx - Sx)
    b = Sy - a * Sx
    x = (0 - b) / a
    print(x)
