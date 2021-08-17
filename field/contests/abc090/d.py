N, K = map(int, input().split())

ans = 0
for b in range(K + 1, N + 1):
    ans += (N // b) * (b - K) + max(0, N % b + min(0, -K + 1))
print(ans)
