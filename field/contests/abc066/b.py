S = input()

l = len(S)
if l % 2 == 0:
    l -= 2
else:
    l -= 1

while l >= 2:
    if S[: l // 2] == S[l // 2 : l]:
        print(l)
        break
    l -= 2
