N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tmp = 0
ans = 0
for i in range(N):
    kill = min(A[i], tmp)
    A[i] -= kill
    ans += kill
    kill = min(A[i], B[i])
    tmp = B[i] - kill
    ans += kill

kill = min(A[-1], tmp)
ans += kill
print(ans)
