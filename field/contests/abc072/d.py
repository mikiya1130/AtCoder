N = int(input())
P = list(map(int, input().split()))

ans = 0
pre = False
for i, p in enumerate(P, 1):
    if i == p and not pre:
        ans += 1
        pre = True
    else:
        pre = False

print(ans)
