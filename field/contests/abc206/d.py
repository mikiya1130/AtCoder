import math
import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = list(map(int, input().split()))


def root(a):
    if a not in tree:
        return a
    else:
        tree[a] = root(tree[a])
        return tree[a]


tree = {}
for i in range(math.ceil(N / 2)):
    if A[i] != A[N-i-1]:
        a = root(A[i])
        b = root(A[N-i-1])
        if a != b:
            tree[a] = b

print(len(tree))
