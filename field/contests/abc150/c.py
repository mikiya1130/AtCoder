import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

for i, t in enumerate(itertools.permutations(range(1, N + 1), N)):
    if t == P:
        nP = i
    if t == Q:
        nQ = i

print(abs(nP - nQ))
