import sys

sys.setrecursionlimit(10000000)

N = int(input())

E = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append((i, b - 1))
    E[b - 1].append((i, a - 1))

color = [None] * (N - 1)
used = set()


def dfs(v, parent_v, parent_c):
    c = 1
    for i, nxt in E[v]:
        if nxt == parent_v:
            continue

        if c == parent_c:
            c += 1
        color[i] = c
        used.add(c)

        dfs(nxt, v, c)
        c += 1


dfs(0, -1, -1)

print(len(used))
for c in color:
    print(c)
