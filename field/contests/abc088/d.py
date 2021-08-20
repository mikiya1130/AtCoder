from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

maze = []
white = 0

maze.append([-1] * (W + 2))
for row in S:
    r = [-1]
    for s in row:
        if s == ".":
            r += [0]
            white += 1
        else:
            r += [-1]
    r += [-1]
    maze.append(r)
maze.append([-1] * (W + 2))

que = deque([(1, 1)])
maze[1][1] = 1
while que:
    i, j = que.popleft()

    if i == H and j == W:
        print(white - maze[i][j])
        break

    if maze[i - 1][j] == 0:
        maze[i - 1][j] = maze[i][j] + 1
        que.append((i - 1, j))
    if maze[i + 1][j] == 0:
        maze[i + 1][j] = maze[i][j] + 1
        que.append((i + 1, j))
    if maze[i][j - 1] == 0:
        maze[i][j - 1] = maze[i][j] + 1
        que.append((i, j - 1))
    if maze[i][j + 1] == 0:
        maze[i][j + 1] = maze[i][j] + 1
        que.append((i, j + 1))
else:
    print(-1)
