def fib(n):
    assert n >= 0

    f = [0, 1] + [None] * (n - 1)

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

A = [-1] + A + [N + 1]
B = []
for a1, a2 in zip(A[:-1], A[1:]):
    n = a2 - a1 - 2
    if n >= 0:
        B.append(n)
    else:
        print(0)
        break
else:
    ans = 1
    for b in B:
        ans *= fib(b + 1)
        ans %= 10 ** 9 + 7
    print(ans)
