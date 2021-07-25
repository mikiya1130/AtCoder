N, M = map(int, input().split())

E = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())

    E[A - 1].append(B - 1)
    E[B - 1].append(A - 1)

que = [0]
next = ["dummy"] + [None] * (N - 1)
for q in que:
    for v in E[q]:
        if next[v] == None:
            next[v] = q
            que.append(v)

print("Yes")
for ans in next[1:]:
    print(ans + 1)
