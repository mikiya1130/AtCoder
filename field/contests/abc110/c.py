S = input()
T = input()

mapping = {}
for s, t in zip(S, T):
    mapping.setdefault(s, t)
    if mapping[s] != t:
        print("No")
        break
else:
    v = mapping.values()
    if len(v) == len(set(v)):
        print("Yes")
    else:
        print("No")
