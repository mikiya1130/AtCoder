N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()
ans = 0
for r in R[-K:]:
    ans = (ans + r) / 2

print(ans)
