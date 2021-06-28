N, K = map(int, input().split())


def g1(n):
    return int(''.join(sorted(list(str(n)))))


def g2(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))


def f(n):
    return g2(n) - g1(n)


ans = N
for _ in range(K):
    ans = f(ans)

print(ans)
