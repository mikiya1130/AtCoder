N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split())) + [None]

ans = 0
tmp = (N, None)
for a in A:
    ans += B[a - 1]
    if tmp[0] + 1 == a:
        ans += tmp[1]
    tmp = (a, C[a - 1])

print(ans)
