N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = None
tmp = 10000
for i in range(N):
    t = T - H[i] * 0.006
    diff = abs(A - t)
    if diff < tmp:
        tmp = diff
        ans = i + 1

print(ans)
