import math

N  = int(input())
A = list(map(int,input().split()))

g = A[0]
for a in A[1:]:
    g = math.gcd(g, a)

print(g)
