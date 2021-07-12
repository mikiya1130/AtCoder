N = int(input())
A = list(map(int, input().split()))

max_a = A[0]
ans = 0
for a in A:
    if a < max_a:
        ans += max_a - a
    else:
        max_a = a

print(ans)
