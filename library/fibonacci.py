# フィボナッチ数
def fib(n):
    assert n >= 0

    f = [0, 1] + [None] * (n - 1)

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
    # listで返す
    # return f
