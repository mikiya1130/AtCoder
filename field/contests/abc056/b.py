W, a, b = map(int, input().split())

ans = 0
ans = max(ans, b - (a + W))
ans = max(ans, a - (b + W))

print(ans)
