A, B = map(int, input().split())

ans = 0
for n in range(A, B + 1):
    l = list(str(n))
    m = list(reversed(l))
    if l == m:
        ans += 1

print(ans)
