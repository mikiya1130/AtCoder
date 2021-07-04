import collections
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

A += [0, N+1]
A.sort()

B = []
for i in range(len(A)-1):
    B.append(A[i+1] - A[i] - 1)
B = collections.Counter(B)
if 0 in B:
    B.pop(0)

if not B:
    print(0)
else:
    k = min(B)

    ans = 0
    for b, n in B.items():
        ans += n * math.ceil(b / k)

    print(ans)
