import math

A, B, C, D = map(int, input().split())

if B == C * D:
    print('-1')
else:
    n = math.ceil(A / (C * D - B))

    if n >= 0:
        print(n)
    else:
        print('-1')
