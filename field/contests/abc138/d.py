N, Q = map(int, input().split())

T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    T[a - 1].append(b - 1)
    T[b - 1].append(a - 1)

V = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    V[p - 1] += x

que = [(0, None)]
for v, parent in que:
    for ch in T[v]:
        if ch != parent:
            V[ch] += V[v]
            que.append((ch, v))

print(*V)
