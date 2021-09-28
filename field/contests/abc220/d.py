N = int(input())
A = list(map(int, input().split()))


def mod_sum(a, b):
    return (a + b) % 10


def mod_mul(a, b):
    return (a * b) % 10


MOD = 998244353

ways = [[0] * 10 for _ in range(N)]
ways[0][A[0]] += 1
for i, a in enumerate(A[1:]):
    for j, w in enumerate(ways[i]):
        s = mod_sum(a, j)
        ways[i + 1][s] = (ways[i + 1][s] + w) % MOD
        m = mod_mul(a, j)
        ways[i + 1][m] = (ways[i + 1][m] + w) % MOD

print(*ways[-1], sep="\n")
