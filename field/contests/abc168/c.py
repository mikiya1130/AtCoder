import math

A, B, H, M = map(int, input().split())

rA = 2 * math.pi * H / 12 + 2 * math.pi * M / 12 / 60
rB = 2 * math.pi * M / 60

theta = rA - rB

ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))
print(ans)
