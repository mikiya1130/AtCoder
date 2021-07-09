import math

N = int(input())
X = list(map(int, input().split()))

absX = [abs(x) for x in X]

print(sum(absX))

d = 0
for x in absX:
    d += x ** 2
print(math.sqrt(d))

print(max(absX))
