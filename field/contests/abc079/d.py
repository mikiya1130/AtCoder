from heapq import heappush, heappop

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]


def dijkstra(s, n, adj):  # (始点, ノード数)
    dist = [10 ** 3] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in enumerate(adj[v]):  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


dist = dijkstra(1, 10, tuple(zip(*C)))

ans = 0
for row in A:
    for a in row:
        if a != -1:
            ans += dist[a]

print(ans)
