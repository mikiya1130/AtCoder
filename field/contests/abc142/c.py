N = int(input())
A = list(map(int, input().split()))
order = range(1, N + 1)

sort = sorted(zip(A, order))
A, order = zip(*sort)

print(*order)
