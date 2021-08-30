import collections

n = int(input())
S = [input() for _ in range(n)]

A = set()
for i in range(n):
    S[i] = collections.Counter(S[i])
    A |= set(S[i].keys())

A = sorted(list(A))
B = {k: 50 for k in A}

for s in S:
    for k in B.keys():
        if k in s:
            B[k] = min(B[k], s[k])
        else:
            B[k] = 0

for k, v in B.items():
    print(k * v, end="")
print()
