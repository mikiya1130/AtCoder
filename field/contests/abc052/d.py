N, A, B = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

ans = 0
for x1, x2 in zip(X[:-1], X[1:]):
    ans += min((x2 - x1) * A, B)

print(ans)
