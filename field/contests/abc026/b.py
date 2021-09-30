import math

N = int(input())
R = [int(input()) for _ in range(N)]

R = sorted(R, reverse=True)

ans = 0
for i, r in enumerate(R):
    if i % 2 == 0:
        ans += r ** 2
    else:
        ans -= r ** 2
ans *= math.pi

print(ans)
