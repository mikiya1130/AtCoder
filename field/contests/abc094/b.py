import bisect

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

idx = bisect.bisect(A, X)
print(min(len(A[:idx]), len(A[idx:])))
