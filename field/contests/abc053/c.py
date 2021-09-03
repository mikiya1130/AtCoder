x = int(input())

ans, mod = divmod(x, 11)
ans *= 2

if 1 <= mod <= 6:
    ans += 1
elif 7 <= mod:
    ans += 2

print(ans)
