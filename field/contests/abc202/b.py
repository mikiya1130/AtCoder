S = [int(s) for s in list(input())]

for i, s in enumerate(S):
    if s == 6:
        S[i] = 9
    elif s == 9:
        S[i] = 6

S.reverse()
S = ''.join(map(str, S))

print(S)
