N, M, C = map(int,input().split())
B = list(map(int,input().split()))

ans = 0
for _ in range(N):
    A = list(map(int,input().split()))
    sum = 0
    for a, b in zip(A, B):
        sum += a * b
    sum += C
    if sum > 0:
        ans += 1

print(ans)
