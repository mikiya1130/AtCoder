N, K, M = map(int, input().split())
A = list(map(int, input().split()))

x = M * N - sum(A)

if x <= K:
    print(max(0, x))
else:
    print(-1)
