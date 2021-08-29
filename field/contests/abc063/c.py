N = int(input())
S = [int(input()) for _ in range(N)]

ans = sum(S)
if ans % 10 == 0:
    ans = 0

for i in range(N):
    tmp = sum(S[:i] + S[i + 1 :])
    if tmp % 10 == 0:
        tmp = 0
    ans = max(ans, tmp)

print(ans)
