N, K = map(int, input().split())

ans = (
    N ** 3
    + 3 * N ** 2
    + 8 * N
    + 2 * K ** 3
    - 3 * (N + 2) * K ** 2
    + (3 * N - 2) * K
    + 12
) // 6

print(ans % (10 ** 9 + 7))
