def cmb(n, r, mod=10 ** 9 + 7):
    if not n >= r >= 0:
        return 0

    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod


N, K = map(int, input().split())

B = K
R = N - K

for i in range(1, K + 1):
    b = B - i
    r = R - (i - 1)

    ans = cmb(i + b - 1, b) * cmb(i + r, r)

    print(ans % (10 ** 9 + 7))
