N = int(input())
A = list(map(int, input().split()))

m = sum(A) / N
m1 = int(m)
m2 = int(m + 1)

ans1 = 0
ans2 = 0
for a in A:
    ans1 += (a - m1) ** 2
    ans2 += (a - m2) ** 2

print(min(ans1, ans2))
