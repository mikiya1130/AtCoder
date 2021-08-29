N, M = map(int, input().split())

MOD = 10 ** 9 + 7


def factorial(n, mod=10 ** 9 + 7):
    a = 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
    return a


if abs(N - M) <= 1:
    ans = factorial(N, MOD) * factorial(M, MOD)
    if N == M:
        ans *= 2
    ans %= MOD
else:
    ans = 0

print(ans)
