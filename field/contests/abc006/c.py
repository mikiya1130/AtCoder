N, M = map(int, input().split())

for a in range(N + 1):
    b = -2 * a + 4 * N - M
    c = a - 3 * N + M
    if b >= 0 and c >= 0:
        print(a, b, c)
        break
else:
    print(-1, -1, -1)
