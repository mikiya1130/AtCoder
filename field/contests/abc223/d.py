import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

E = [[] for _ in range(N)]
In = [0] * N
for a, b in AB:
    E[a - 1].append(b - 1)
    In[b - 1] += 1

Que = [i for i, n in enumerate(In) if n == 0]

heapq.heapify(Que)
ans = []
while Que:
    p = heapq.heappop(Que)
    ans.append(p + 1)

    for v in E[p]:
        In[v] -= 1
        if In[v] == 0:
            heapq.heappush(Que, v)

if len(ans) == N:
    print(*ans)
else:
    print(-1)
