import math

A, B, W = map(int, input().split())

W *= 1000
min = math.ceil(W / B)
max = math.floor(W / A)

if min > max:
    print('UNSATISFIABLE')
else:
    print(min, max)
