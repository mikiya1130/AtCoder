N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

Z = tuple(range(X + 1, Y + 1))
xr = max(x)
yl = min(y)

for z in Z:
    if xr < z <= yl:
        print("No War")
        break
else:
    print("War")
