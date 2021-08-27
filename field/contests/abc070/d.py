from heapq import heappush, heappop

INF = 10 ** 15


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


N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N - 1)]
Q, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(Q)]

E = [[] for _ in range(N)]
for a, b, c in ABC:
    E[a - 1].append((b - 1, c))
    E[b - 1].append((a - 1, c))

dist = dijkstra(K - 1, N, E)

for x, y in XY:
    print(dist[x - 1] + dist[y - 1])
