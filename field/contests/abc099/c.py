N = int(input())

dp = [10 ** 6] * (N + 1)
dp[0] = 0

for i in range(N):
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    x = 6
    while x <= i + 1:
        dp[i + 1] = min(dp[i + 1], dp[i + 1 - x] + 1)
        x *= 6

    x = 9
    while x <= i + 1:
        dp[i + 1] = min(dp[i + 1], dp[i + 1 - x] + 1)
        x *= 9

print(dp[N])
