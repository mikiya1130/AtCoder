import collections

N = int(input())
S = input().split()
S = collections.Counter(S)
if len(S) == 3:
    print("Three")
else:
    print("Four")
