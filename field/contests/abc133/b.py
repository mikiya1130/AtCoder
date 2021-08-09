import itertools

N, D = map(int, input().split())

X = []
for _ in range(N):
    x = list(map(int, input().split()))
    X.append(x)

Square = [i * i for i in range(127)]

ans = 0
for Y, Z in itertools.combinations(X, 2):
    sum = 0
    for i in range(D):
        sum += (Y[i] - Z[i]) ** 2
    if sum in Square:
        ans += 1

print(ans)
