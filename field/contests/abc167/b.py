A, B, C, K = map(int, input().split())

if B >= K - A:
    print(min(A, K))
else:
    print(A - (K - A - B))
