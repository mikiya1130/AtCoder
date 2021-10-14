import collections

N = int(input())
S = [input() for _ in range(N)]

S = collections.Counter(S)
S = sorted(S.items(), reverse=True, key=lambda x: x[1])

print(S[0][0])
