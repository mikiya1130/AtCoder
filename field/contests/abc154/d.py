N, K = map(int, input().split())
P = list(map(int, input().split()))

P = [(p + 1) / 2 for p in P]

ans = sum(P[:K])
s = ans
for i in range(N - K):
    s += P[i + K] - P[i]
    ans = max(ans, s)

print(ans)
