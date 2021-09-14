N = int(input())
K = int(input())
X = int(input())
Y = int(input())

K = min(N, K)

print(K * X + (N - K) * Y)
