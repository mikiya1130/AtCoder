S = tuple(map(int, tuple(input())))

l = len(S)
ans = 0
for i in range(2 ** (l - 1)):
    T = []
    tmp = S[0]
    for j in range(l - 1):
        if i >> j & 1:
            tmp = tmp * 10 + S[j + 1]
        else:
            T += [tmp]
            tmp = S[j + 1]
    T += [tmp]
    ans += sum(T)

print(ans)
