N = int(input())

S1 = set()
S2 = set()
for i in range(N):
    s = input()
    if s[0] != '!':
        S1.add(s)
    else:
        S2.add(s[1:])

S = S1 & S2
if len(S):
    print(S.pop())
else:
    print('satisfiable')
