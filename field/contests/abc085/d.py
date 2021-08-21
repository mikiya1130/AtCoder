N, H = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

a = max([ab[0] for ab in AB])
B = [ab[1] for ab in AB if ab[1] > a]

ans = 0
for b in sorted(B, reverse=True):
    H -= b
    ans += 1
    if H <= 0:
        break
else:
    ans += (H + a - 1) // a

print(ans)
