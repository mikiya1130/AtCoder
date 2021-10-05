a, b = [int(input()) for _ in range(2)]

s = b
while a > s:
    s += b

print(s - a)
