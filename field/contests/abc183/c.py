import itertools

N, K = map(int, input().split())

T = []
for _ in range(N):
    t = list(map(int, input().split()))
    T.append(t)

ans = 0
for order in itertools.permutations(range(1, N)):
    order = (0,) + order + (0,)
    time = 0
    for i in range(N):
        time += T[order[i]][order[i + 1]]
    if time == K:
        ans += 1

print(ans)
