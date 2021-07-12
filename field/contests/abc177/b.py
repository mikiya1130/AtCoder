S = input()
T = input()

len_s = len(S)
len_t = len(T)

ans = len_t
for i in range(len_s - len_t + 1):
    n = 0
    for j in range(len_t):
        if S[i + j] != T[j]:
            n += 1

    ans = min(ans, n)

print(ans)
