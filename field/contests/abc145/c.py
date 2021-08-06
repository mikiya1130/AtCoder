import itertools

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

dist = 0
cnt = 0
for path in itertools.permutations(range(N), N):
    cnt += 1
    for a, b in zip(path[:-1], path[1:]):
        x1, y1 = P[a]
        x2, y2 = P[b]
        dist += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(dist / cnt)
