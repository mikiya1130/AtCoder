import itertools
INF = 1 << 40

N, M = map(int, input().split())

l = [[INF] * N for _ in range(N)]
for i in range(N):
    l[i][i] = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    l[A-1][B-1] = C

ans = 0
for k in range(N):
    cost = [[0] * N for _ in range(N)]
    for s, t in itertools.product(range(N), range(N)):
        cost[s][t] = min(l[s][t], l[s][k] + l[k][t])
        if cost[s][t] < INF:
            ans += cost[s][t]
    l = cost

print(ans)
