import itertools

S = input()
N = int(input())

L = []
for s in itertools.product(S, repeat=2):
    L.append("".join(s))

print(L[N-1])
