N = int(input())

ans = 0
for i in range(1, N + 1):
    n = N // i
    ans += (n / 2) * (2 * i + (n - 1) * i)

print(int(ans))
