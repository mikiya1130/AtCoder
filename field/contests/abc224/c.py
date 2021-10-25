import itertools

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b, c in itertools.combinations(XY, 3):
    if (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]):
        ans += 1

print(ans)
