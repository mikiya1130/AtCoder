import itertools

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

S = set()
for (x1, y1), (x2, y2) in itertools.combinations(XY, 2):
    if x1 != x2:
        S.add((y2 - y1) / (x2 - x1))
    else:
        S.add(10 ** 9 + 1)

print(len(S) * 2)
