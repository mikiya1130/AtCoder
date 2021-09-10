S = input()

prev = S[0]
ans = 0
for s in S:
    if prev != s:
        ans += 1
        prev = s

print(ans)
