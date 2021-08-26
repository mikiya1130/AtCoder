import sys

sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
E = [[] for _ in range(N)]
AB = []
for _ in range(M):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)
    AB.append((a - 1, b - 1))

seen_v = [False] * N
ord = [None] * N
lowlink = [None] * N
ans = 0
k = 0


def dfs(v, pre):
    global k
    global ans

    seen_v[v] = True
    ord[v] = lowlink[v] = k
    k += 1

    for to in E[v]:
        if ord[to] is None:
            dfs(to, v)
            lowlink[v] = min(lowlink[v], lowlink[to])
        if to != pre:
            lowlink[v] = min(lowlink[v], ord[to])

        if ord[v] < lowlink[to]:
            ans += 1


dfs(0, -1)

print(ans)
