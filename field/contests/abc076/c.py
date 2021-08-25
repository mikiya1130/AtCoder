S = input()
T = input()

lS = len(S)
lT = len(T)

for i in range(lS - lT, -1, -1):
    for j in range(lT):
        if S[i + j] != "?" and S[i + j] != T[j]:
            break
    else:
        ans = S[:i] + T + S[i + lT :]
        ans = ans.replace("?", "a")
        print(ans)
        break
else:
    print("UNRESTORABLE")
