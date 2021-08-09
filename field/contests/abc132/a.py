import collections

S = input()
L = collections.Counter(S)
if tuple(L.values()) == (2, 2):
    print("Yes")
else:
    print("No")
