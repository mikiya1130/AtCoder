N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    L = list(str(i))
    s = sum([int(l) for l in L])
    if A <= s <= B:
        ans += i

print(ans)
