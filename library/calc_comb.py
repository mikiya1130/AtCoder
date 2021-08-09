# 組み合わせ
from operator import mul
from functools import reduce


def cmb(n, r):
    assert n >= r >= 0

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


# ------------------------------


def cmb(n, r, mod):
    assert n >= r >= 0

    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10 ** 9 + 7  # 出力の制限
N = 10 ** 6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

cmb(n, r, mod)

# ------------------------------


def cmb(n, r, mod=10 ** 9 + 7):
    assert n >= r >= 0

    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod


# ------------------------------

# 重複組み合わせ
def H(n, r, mod=10 ** 9 + 7):
    return cmb(n + r - 1, r, mod)
