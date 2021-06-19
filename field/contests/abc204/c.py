import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

load = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    load[A-1].append(B-1)


def dfs(i):
    if tmp[i] == True:
        return
    tmp[i] = True
    for ii in load[i]:
        dfs(ii)


ans = 0
for i in range(N):
    tmp = [False] * N
    dfs(i)
    ans += sum(tmp)

print(ans)
