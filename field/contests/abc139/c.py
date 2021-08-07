N = int(input())
H = list(map(int, input().split()))

ans = 0
move = 0
left = 0
for h in H:
    if left >= h:
        move += 1
    else:
        move = 0

    ans = max(ans, move)
    left = h

print(ans)
