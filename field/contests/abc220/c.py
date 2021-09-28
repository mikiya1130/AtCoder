import itertools, bisect

N = int(input())
A = list(map(int, input().split()))
X = int(input())

A = tuple(itertools.accumulate(A))

oriX = X
ans, X = divmod(X, A[-1])
ans *= N
ans += bisect.bisect_right(A, X) + 1

print(ans)
