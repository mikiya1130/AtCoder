N, M = map(int, input().split())

road = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())

    road[A - 1].append(B - 1)
    road[B - 1].append(A - 1)

que = [0]
hour = [None] * N
count = [0] * N

hour[0] = 0
count[0] = 1

for q in que:
    for r in road[q]:
        if hour[r] is None:
            hour[r] = hour[q] + 1
            count[r] = count[q]
            que.append(r)
        elif hour[r] == hour[q] + 1:
            count[r] += count[q]
            count[r] %= 10 ** 9 + 7

print(count[N - 1])
