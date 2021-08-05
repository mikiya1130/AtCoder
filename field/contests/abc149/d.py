N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

chg = [False] * N
ans = 0
for i in range(N):
    if i - K >= 0:
        c = chg[i - K]
        t = T[i - K]
    else:
        c = False
        t = None

    if T[i] == "r" and (c or t != "r"):
        ans += P
    elif T[i] == "s" and (c or t != "s"):
        ans += R
    elif T[i] == "p" and (c or t != "p"):
        ans += S
    else:
        chg[i] = True

print(ans)
