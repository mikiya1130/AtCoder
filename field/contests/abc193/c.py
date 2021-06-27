import math

N = int(input())

max = math.floor(math.sqrt(N))

s = set()
for i in range(2, max + 1):
    x = i ** 2
    while x <= N:
        s.add(x)
        x *= i

print(N - len(s))
