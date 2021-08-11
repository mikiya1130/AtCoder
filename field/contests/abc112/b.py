N, T = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(N)]

ans = 1001
for c, t in CT:
    if t <= T and c < ans:
        ans = c

if ans == 1001:
    print("TLE")
else:
    print(ans)
