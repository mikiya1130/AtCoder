S = input()

ans = 0
len = 0
for s in S:
    if s == "A" or s == "C" or s == "G" or s == "T":
        len += 1
    else:
        ans = max(ans, len)
        len = 0
ans = max(ans, len)

print(ans)
