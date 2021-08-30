N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

cnt = [0] * N
for a, b in AB:
    cnt[a - 1] += 1
    cnt[b - 1] += 1

for c in cnt:
    print(c)
