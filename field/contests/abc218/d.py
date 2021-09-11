import itertools
import bisect

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

XY.sort()
l = len(XY)
ans = 0
for (x0, y0), (x1, y1) in itertools.combinations(XY, 2):
    if x0 == x1 or y0 == y1:
        continue
    idx1 = bisect.bisect_left(XY, (x0, y1))
    idx2 = bisect.bisect_left(XY, (x1, y0))
    if idx1 < l and idx2 < l and (x0, y1) == XY[idx1] and (x1, y0) == XY[idx2]:
        ans += 1

print(ans // 2)
