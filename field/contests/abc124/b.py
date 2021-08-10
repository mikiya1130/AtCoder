N = int(input())
H = list(map(int, input().split()))

ans = 0
max = 0
for h in H:
    if max <= h:
        ans += 1
        max = h

print(ans)
