N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for a in A:
    ans += (D - 1) // a + 1
ans += X

print(ans)
