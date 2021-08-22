import math
import bisect


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True


def list_prime(n):
    if n <= 1:
        return []
    A = [2] + list(range(3, n + 1, 2))
    B = list()
    while A[0] ** 2 <= n:
        tmp = A[0]
        B.append(tmp)
        A = [a for a in A if a % tmp != 0]
    return B + A


P = list_prime(10 ** 5)
P = [p for p in P if is_prime((p + 1) / 2)]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    idx_l = bisect.bisect_left(P, l)
    idx_r = bisect.bisect_right(P, r)

    print(idx_r - idx_l)
