n = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
for a in A:
    if a >= 9:
        ans += a - 9
    elif a >= 7:
        ans += a - 7
    elif a >= 3:
        ans += a - 3
    else:
        ans += a - 1

print(ans)
