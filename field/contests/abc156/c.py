N = int(input())
X = list(map(int, input().split()))

sumX = sum(X)
p = int((sumX / N) + 0.5)

ans = 0
for x in X:
    ans += (x - p) ** 2

print(ans)
