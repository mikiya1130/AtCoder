S = input()

lenS = len(S)
N = [0] * lenS

n = 0
for i in range(lenS):
    if S[i] == "L":
        n += 1
        N[i] = n
    else:
        n = 0
for i in range(lenS - 1, -1, -1):
    if S[i] == "R":
        n += 1
        N[i] = n
    else:
        n = 0

ans = [0] * lenS
for i, (s, n) in enumerate(zip(S, N)):
    if s == "L":
        if n % 2 == 0:
            ans[i - n] += 1
        else:
            ans[i - n + 1] += 1
    elif s == "R":
        if n % 2 == 0:
            ans[i + n] += 1
        else:
            ans[i + n - 1] += 1

print(*ans)
