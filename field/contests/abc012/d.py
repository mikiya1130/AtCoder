from heapq import heappush, heappop

N, M = map(int, input().split())
ABT = [list(map(int, input().split())) for _ in range(M)]

adj = [[] for _ in range(N)]
for a, b, t in ABT:
    adj[a - 1].append((b - 1, t))
    adj[b - 1].append((a - 1, t))

INF = 10 ** 15

# s:始点
# n:ノード数
# adj:エッジ [[(to, cost), ...], ...]
def dijkstra(s, n, adj):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


D = []
for n in range(N):
    D.append(max(dijkstra(n, N, adj)))

print(min(D))
