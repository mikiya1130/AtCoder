import math

X, Y, A, B = map(int, input().split())

exp = 0

while X < Y:
    tmp = X * A
    if tmp - X < B:
        X = tmp
        exp += 1
    else:
        break

exp += (Y - X - 1) // B

print(exp)
