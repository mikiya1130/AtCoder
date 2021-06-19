N, K = map(int, input().split())

print(sum(list(range(1, N+1))) * K * 100 + sum(list(range(1, K+1))) * N)
