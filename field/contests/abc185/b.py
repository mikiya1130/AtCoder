N, M, T = map(int, input().split())

n = N
pre = 0
for i in range(M):
    A, B = map(int, input().split())

    n -= A - pre
    if n <= 0:
        print('No')
        break

    n += B - A
    n = min(n, N)
    pre = B
else:
    n -= T - pre
    if n > 0:
        print('Yes')
    else:
        print('No')
