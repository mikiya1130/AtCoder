import sys

sys.setrecursionlimit(1000000)

N = int(input())

E = [[] for _ in range(N)]

for _ in range(N - 1):
    A, B = map(int, input().split())
    E[A - 1].append(B - 1)
    E[B - 1].append(A - 1)

for i in range(N):
    E[i].sort()


def dfs(v, parent):
    print(v + 1, end=" ")
    for nxt in E[v]:
        if nxt != parent:
            dfs(nxt, v)
            print(v + 1, end=" ")


dfs(0, None)
print()
