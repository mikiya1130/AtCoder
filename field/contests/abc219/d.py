N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[301] * (Y + 1) for _ in range((X + 1))]
dp[0][0] = 0

for a, b in AB:
    for x in range(X, -1, -1):
        for y in range(Y, -1, -1):
            dp[x][y] = min(dp[x][y], dp[max(0, x - a)][max(0, y - b)] + 1)

if dp[X][Y] != 301:
    print(dp[X][Y])
else:
    print(-1)
