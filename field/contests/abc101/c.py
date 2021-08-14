def ceil(a, b):
    return (a + b - 1) // b


N, K = map(int, input().split())
A = list(map(int, input().split()))
print(ceil(N - 1, K - 1))
