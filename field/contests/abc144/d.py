import math

a, b, x = map(int, input().split())

if 2 * x < a * a * b:
    c = b
    d = (x * 2) / (a * b)
else:
    h = x / (a ** 2)
    c = 2 * (b - h)
    d = a

e2 = c ** 2 + d ** 2
e = e2 ** 0.5

cosC = (d ** 2 + e2 - c ** 2) / (2 * d * e)
print(math.degrees(math.acos(cosC)))
