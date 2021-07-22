import math


# nが素数か判定
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True


# n以下の素数をlistで列挙
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
