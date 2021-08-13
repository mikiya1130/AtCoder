N, K = map(int, input().split())
X = list(map(int, input().split()))

T = []
for i in range(N - K + 1):
    d1 = min(abs(X[i]), abs(X[i + K - 1]))
    d2 = X[i + K - 1] - X[i]
    T.append(d1 + d2)

print(min(T))
