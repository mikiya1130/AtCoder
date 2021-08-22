N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

lS = len(set(S))
lT = len(set(T))
if lS == 1 and lT == 1:
    if S[0] == T[0]:
        print(len(T))
    else:
        print(-1)
elif lS == 1 and lT == 2:
    print(-1)
elif lS == 2 and lT == 1:
    ans = len(T)
    if S[0] != T[0]:
        ans += min(S.index(1 - S[0]), list(reversed(S)).index(1 - S[0]) + 1)
    print(ans)
elif lS == 2 and lT == 2:
    ans = 0
    a1 = S[0]
    n = min(S.index(1 - S[0]), list(reversed(S)).index(1 - S[0]) + 1)
    for t in T:
        if t != a1:
            ans += n
            n = 1
            a1 = 1 - a1
        ans += 1
    print(ans)
