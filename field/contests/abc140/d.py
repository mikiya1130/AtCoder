N, K = map(int, input().split())
S = input()

ans = 0
s = S[0]
sub = False
for i in range(N - 1):
    if S[i] == S[i + 1]:
        ans += 1
    elif S[i] == s and K > 0:
        ans += 2
        K -= 1
        sub = True
    elif S[i] != s:
        sub = False

if sub:
    ans -= 1

print(ans)
