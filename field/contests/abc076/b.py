N = int(input())
K = int(input())

n = 0
while 2 ** n < K:
    n += 1

n = min(n, N)

print(2 ** n + K * (N - n))
