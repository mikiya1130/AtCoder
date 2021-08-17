import collections, itertools

N = int(input())
S = [input() for _ in range(N)]

S = [s[0] for s in S if s[0] in "MARCH"]
S = dict(collections.Counter(S))

if len(S) <= 2:
    print(0)
else:
    ans = 0
    for a, b, c in itertools.combinations(S.values(), 3):
        ans += a*b*c
    print(ans)
