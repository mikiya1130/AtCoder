import sys
sys.setrecursionlimit(10000000)

_ = int(input())
A = list(map(int, input().split()))


def dfs(list):
    m = min(list)
    l = len(list)

    n = m * l

    i = list.index(m)

    if i >= 1:
        n = max(n, dfs(list[:i]))
    if i+1 < l:
        n = max(n, dfs(list[i+1:]))

    return n


print(dfs(A))
