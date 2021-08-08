import bisect

H, W, N = map(int, input().split())

setH = set()
setW = set()
Card = []
for _ in range(N):
    A, B = map(int, input().split())
    setH.add(A)
    setW.add(B)
    Card.append((A, B))

setH = tuple(sorted(setH))
setW = tuple(sorted(setW))

for (a, b) in Card:
    x = bisect.bisect_right(setH, a)
    y = bisect.bisect_right(setW, b)
    print(x, y)
