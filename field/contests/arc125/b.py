N = int(input())

ans = 0
for i in range(1, N):
    n = i * i
    if n > N:
        break

    ans += (N - n) // (2 * i) + 1

if N == 1:
    ans = 1

print(ans % 998244353)
