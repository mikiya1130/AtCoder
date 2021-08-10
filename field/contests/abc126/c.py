import math

N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    n = max(0, math.ceil(math.log2(K / i)))
    ans += 1 / 2 ** n

print(ans / N)
