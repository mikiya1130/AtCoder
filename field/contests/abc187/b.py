import itertools

N = int(input())

Z = []
for i in range(N):
    x, y = map(int, input().split())
    Z.append((x, y))

ans = 0
for i, j in itertools.combinations(Z, 2):
    x = j[0] - i[0]
    y = j[1] - i[1]

    if x == 0:
        continue

    a = y / x
    if -1 <= a <= 1:
        ans += 1

print(ans)
