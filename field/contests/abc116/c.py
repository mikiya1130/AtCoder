N = int(input())
H = list(map(int,input().split()))

pre = 0
ans = 0
for h in H:
    if pre < h:
        ans += h - pre
    pre = h

print(ans)
