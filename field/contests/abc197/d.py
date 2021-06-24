import math

N = int(input())
x0, y0 = map(int, input().split())
xN2, yN2 = map(int, input().split())

theta = 360 / N
Cx = (x0 + xN2) / 2
Cy = (y0 + yN2) / 2

x1 = math.cos(math.radians(theta)) * (x0 - Cx) - \
    math.sin(math.radians(theta)) * (y0 - Cy) + Cx
y1 = math.sin(math.radians(theta)) * (x0 - Cx) + \
    math.cos(math.radians(theta)) * (y0 - Cy) + Cy

print(x1, y1)
