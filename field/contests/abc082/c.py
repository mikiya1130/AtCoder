import collections

N = int(input())
A = list(map(int, input().split()))

A = collections.Counter(A)

ans = 0
for k, v in A.items():
    if k < v:
        ans += v - k
    elif k > v:
        ans += v

print(ans)
