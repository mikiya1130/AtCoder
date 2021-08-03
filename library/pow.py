# 累乗(x**n)を高速に計算
# 繰り返し2乗法
# O(log n)


def pow_k(x, n, mod=10 ** 9 + 7):
    if n == 0:
        return 1

    k = 1
    while n > 0:
        if n % 2 != 0:
            k = k * x % mod
        x = x * x % mod
        n //= 2

    return k
