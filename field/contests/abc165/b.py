X = int(input())

x = 100
i = 0
while x < X:
    x += x // 100
    i += 1

print(i)
