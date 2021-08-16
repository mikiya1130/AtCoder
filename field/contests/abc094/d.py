def get_nearest_index(L, num):
    idx = None

    min_diff = None
    for i, l in enumerate(L):
        diff = abs(l - num)
        if min_diff is None or diff < min_diff:
            idx = i
            min_diff = diff

    return idx


N = int(input())
A = list(map(int, input().split()))

A.sort()
n = A[-1]
r = A[get_nearest_index(A, n / 2)]

print(n, r)
