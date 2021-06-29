N = int(input())

count = 0
n = 1
while True:
    a = (- n ** 2 + n + 2 * N) / (2 * n)
    if a <= 0:
        break
    if a.is_integer():
        count += 1
    n += 1

print(count * 2)
