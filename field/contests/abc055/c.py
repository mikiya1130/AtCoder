N, M = map(int, input().split())

ans = 0
if N * 2 > M:
    ans += M // 2
else:
    ans += N
    M -= N * 2
    ans += M // 4

print(ans)
