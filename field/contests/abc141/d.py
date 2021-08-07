import math
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
n = int(math.log2(A[-1]))
B = [[] for _ in range(n + 1)]
for a in A:
    B[int(math.log2(a))].append(a)

for _ in range(M):
    while B:
        X = B[-1]
        if X:
            break
        B.pop(-1)
    else:
        X = [1]

    x = X.pop(-1)
    if x != 1:
        bisect.insort(B[-2], x // 2)

ans = 0
for X in B:
    ans += sum(X)

print(ans)
