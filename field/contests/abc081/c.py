import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = collections.Counter(A)
A = sorted(A.values(), reverse=True)

print(sum(A[K:]))
