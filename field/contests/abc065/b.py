import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
A = [int(input()) - 1 for _ in range(N)]

seen = [False] * N


def push(a, n=0):
    if a == 1:
        return n

    if seen[a]:
        return -1

    seen[a] = True

    return push(A[a], n + 1)


print(push(0))
