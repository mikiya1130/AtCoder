def len(l):
    if l == 0:
        return 1
    return 2 * len(l - 1) + 3


def num_patty(l, x):
    if l == 0 and x == 1:
        return 1

    n = len(l)
    center = n // 2 + 1
    assert 1 <= x <= n

    if x == 1:
        return 0
    elif 1 < x < center:
        return num_patty(l - 1, x - 1)
    elif x == center:
        return num_patty(l - 1, center - 2) + 1
    elif center < x < n:
        return num_patty(l - 1, center - 2) + 1 + num_patty(l - 1, x - center)
    elif x == n:
        return num_patty(l - 1, center - 2) * 2 + 1


N, X = map(int, input().split())
print(num_patty(N, X))
