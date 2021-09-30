import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
B = [int(input()) for _ in range(N - 1)]

T = [[] for _ in range(N)]
for i, b in enumerate(B):
    T[b - 1].append(i + 1)


def samary(t):
    if t == []:
        return 1

    l = []
    for p in t:
        l.append(samary(T[p]))

    return max(l) + min(l) + 1


S = [1] * N
print(samary(T[0]))
