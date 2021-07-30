K = int(input())

N = []


def dfs(s, d):
    N.append(int(s))
    if d <= 9:
        n = int(s[-1])
        if n != 0:
            dfs(s + str(n - 1), d + 1)
        dfs(s + str(n), d + 1)
        if n != 9:
            dfs(s + str(n + 1), d + 1)


for i in range(1, 10):
    dfs(str(i), 1)

N = sorted(N)
print(N[K - 1])
