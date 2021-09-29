import collections

S = input()
S = dict(collections.Counter(S))

for k in ("A", "B", "C", "D", "E", "F"):
    if k in S:
        print(S[k], end="")
    else:
        print(0, end="")
    if k != "F":
        print(" ", end="")
print()
