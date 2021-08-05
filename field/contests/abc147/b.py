S = input()
l = len(S)

ans = 0
for i in range(l // 2):
    if S[i] != S[l - i - 1]:
        ans += 1

print(ans)
