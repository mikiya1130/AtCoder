import bisect


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


X = int(input())

li = list_prime(100003)
idx = bisect.bisect_left(li, X)

print(li[idx])
