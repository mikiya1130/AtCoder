import collections

N = int(input())
A = [int(input()) for _ in range(N)]

A = collections.Counter(A)

ans = 0
for a in A.values():
    ans += a % 2

print(ans)
