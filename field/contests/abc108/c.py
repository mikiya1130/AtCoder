N, K = map(int, input().split())

n = N // K
ans = n ** 3
if K % 2 == 0:
    if N % K >= K // 2:
        n += 1
    ans += n ** 3

print(ans)
