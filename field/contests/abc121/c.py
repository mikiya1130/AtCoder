N, M = map(int,input().split())

C = []
for _ in range(N):
    A, B = map(int,input().split())
    C.append((A, B))
C.sort()

ans = 0
m = 0
for a, b in C:
    if m + b < M:
        m += b
        ans += a * b
    else:
        ans += a * (M-m)
        break

print(ans)
