import math

X = int(input())

ans = 1
for b in range(2, int(math.sqrt(X)) + 1):
    p = int(math.log(X, b))
    if b ** (p + 1) <= X:
        p += 1
    ans = max(ans, b ** p)

print(ans)
