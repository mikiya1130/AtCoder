N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

for a, b in AB:
    ans = None
    ans_dist = 10 ** 9
    for i, (c, d) in enumerate(CD, start=1):
        dist = abs(a - c) + abs(b - d)
        if dist < ans_dist:
            ans = i
            ans_dist = dist
    print(ans)
