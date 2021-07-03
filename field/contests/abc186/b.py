H, W = map(int, input().split())

A = []
m = 101
for i in range(H):
    a = list(map(int, input().split()))
    m = min(m, min(a))
    A.append(a)

ans = 0
for a in A:
    for i in a:
        ans += i - m

print(ans)
