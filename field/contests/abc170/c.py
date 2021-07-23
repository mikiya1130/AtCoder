import bisect

X, N = map(int, input().split())
P = set(map(int, input().split()))

notP = list(set(range(0, 102)) - P)

if X in notP:
    print(X)
else:
    i = bisect.bisect(notP, X)
    if X - notP[i - 1] <= notP[i] - X:
        print(notP[i - 1])
    else:
        print(notP[i])
