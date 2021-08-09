n = int(input())
P = list(map(int, input().split()))

diff = [P[i] - P[i + 1] for i in range(n - 1)]
dot = [diff[i] * diff[i + 1] for i in range(n - 2)]

ans = 0
for i, d in enumerate(dot):
    if d > 0:
        ans += 1
    elif d == 0:
        if diff[i] - diff[i + 1] < 0:
            ans += 1

print(ans)
