N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
n = min(K, N - K + 1)
for i in range(1, n):
    ans += i * (A[i - 1] + A[N - i])
ans += n * sum(A[n - 1 : n - 1 + (N - (n - 1) * 2)])

print(ans)
