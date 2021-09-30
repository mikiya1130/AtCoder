import collections

L = list(map(int, input().split()))

L = collections.Counter(L)
for l, n in L.items():
    if n % 2 == 1:
        print(l)
        break
