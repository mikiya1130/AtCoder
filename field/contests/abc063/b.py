import collections

S = input()
S = collections.Counter(S)

if set(S.values()) == {1}:
    print("yes")
else:
    print("no")
