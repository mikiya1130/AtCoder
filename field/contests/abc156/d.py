def pow_k(x, n):
    k = 1
    while n > 0:
        if n % 2 != 0:
            k = k * x % mod
        x = x * x % mod
        n //= 2

    return k


def cmb(n, r):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod


n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

ans = pow_k(2, n) - 1
ans -= cmb(n, a)
ans -= cmb(n, b)
ans %= mod

print(ans)
