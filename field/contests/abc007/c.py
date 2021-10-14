from queue import Queue

r, c = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
C = [input() for _ in range(r)]

E = [[[] for _ in range(c)] for _ in range(r)]
seen = [[False] * c for _ in range(r)]
for rr in range(r):
    for cc in range(c):
        if C[rr][cc] == ".":
            if rr + 1 < r and C[rr + 1][cc] == ".":
                E[rr][cc].append((rr + 1, cc))
            if 0 <= rr - 1 and C[rr - 1][cc] == ".":
                E[rr][cc].append((rr - 1, cc))
            if cc + 1 < c and C[rr][cc + 1] == ".":
                E[rr][cc].append((rr, cc + 1))
            if 0 <= cc - 1 and C[rr][cc - 1] == ".":
                E[rr][cc].append((rr, cc - 1))

que = Queue()
que.put((sx - 1, sy - 1, 0))
seen[sx - 1][sy - 1] = True
while not que.empty():
    x, y, n = que.get()
    for xx, yy in E[x][y]:
        if seen[xx][yy]:
            continue

        if xx == gx - 1 and yy == gy - 1:
            print(n + 1)
            que = Queue()
            break

        que.put((xx, yy, n + 1))
        seen[xx][yy] = True
