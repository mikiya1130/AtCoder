# ダイクストラ法
# 重み付き単一始点最短経路

from heapq import heappush, heappop

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
