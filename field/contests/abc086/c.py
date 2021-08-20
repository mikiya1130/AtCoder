N = int(input())

pre_t, pre_x, pre_y = 0, 0, 0
ans = "Yes"
for _ in range(N):
    t, x, y = map(int, input().split())

    dt = t - pre_t
    dx = abs(x - pre_x)
    dy = abs(y - pre_y)

    if dt < dx + dy:
        ans = "No"

    if dt % 2 != (dx + dy) % 2:
        ans = "No"

    pre_t = t
    pre_x = x
    pre_y = y

print(ans)
