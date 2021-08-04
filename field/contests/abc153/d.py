import math

H = int(input())

x = math.floor(math.log2(H))
x = x + 1
ans = 2 ** x - 1

print(ans)
