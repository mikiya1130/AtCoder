A, B, N = map(int, input().split())

if B == 1:
    print(0)
else:

    def y(x):
        return A * x // B - A * (x // B)

    ans = y(N)
    for x in range(B - 1, N + 1, B):
        ans = max(ans, y(x))

    print(ans)
