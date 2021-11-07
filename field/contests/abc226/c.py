N = int(input())
TKA = [list(map(int, input().split())) for _ in range(N)]

S = set([N])
ans = 0
for i, (T, K, *A) in enumerate(reversed(TKA)):
    if N - i in S:
        S.remove(N - i)
        ans += T
        S |= set(A)

print(ans)
