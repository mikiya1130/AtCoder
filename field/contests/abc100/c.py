N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    cnt = 0
    while a % 2 == 0:
        cnt += 1
        a //= 2
    ans += cnt

print(ans)
