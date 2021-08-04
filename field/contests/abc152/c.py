N = int(input())
P = list(map(int, input().split()))

_min = N + 1
ans = 0
for p in P:
    if _min >= p:
        ans += 1
        _min = p

print(ans)
