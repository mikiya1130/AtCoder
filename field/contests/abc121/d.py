def f(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x+1
    elif x % 4 == 3:
        return 0

A, B = map(int,input().split())

a = f(A-1)
b = f(B)

print(a ^ b)
