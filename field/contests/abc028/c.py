import itertools

N = list(map(int, input().split()))

S = set()
for n in itertools.combinations(N, 3):
    S.add(sum(n))
S = sorted(S, reverse=True)

print(S[2])
