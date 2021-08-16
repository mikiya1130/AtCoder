N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

X -= sum(M)
ans = len(M)

m = min(M)
ans += X // m

print(ans)
