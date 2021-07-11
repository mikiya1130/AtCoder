import math

N = int(input())

ans = 0
for i in range(1, N):
    ans += int(math.ceil(N / i)) - 1

print(ans)
