N = int(input())
W = list(map(int, input().split()))

L, R = 0, sum(W)
ans = R

for w in W:
    L, R = L + w, R - w
    ans = min(ans, abs(L - R))

print(ans)
