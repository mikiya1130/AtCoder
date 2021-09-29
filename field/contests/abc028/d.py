N, K = map(int, input().split())

l = K - 1
r = N - K
n = (l * r * 6) + (l * 3) + (r * 3) + 1

print(n / (N ** 3))
