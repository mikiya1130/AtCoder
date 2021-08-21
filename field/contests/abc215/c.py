import itertools

S, K = input().split()
K = int(K)

S = list(S)
S = itertools.permutations(S, len(S))
S = ["".join(s) for s in S]
S = set(S)
S = sorted(S)

print(S[K - 1])
