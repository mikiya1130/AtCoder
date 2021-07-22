import itertools
import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

accA = list(itertools.accumulate(A))
accB = list(itertools.accumulate(B))

n = bisect.bisect_right(accA, K)
m = 0
ans = 0

while n >= 0:
    if n == 0:
        m = bisect.bisect_right(accB, K)
    else:
        m = bisect.bisect_right(accB, K - accA[n - 1])

    ans = max(ans, n + m)

    n -= 1

print(ans)
