X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    print(0)
elif X * 2 < Y or Y * 2 < X:
    print(0)
else:

    def cmb(n, r, mod=10 ** 9 + 7):
        p, q = 1, 1
        for i in range(r):
            p = p * (n - i) % mod
            q = q * (i + 1) % mod
        return p * pow(q, mod - 2, mod) % mod

    n = (X + Y) // 3
    r = X - n
    print(cmb(n, r))
