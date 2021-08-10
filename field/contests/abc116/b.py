def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())

seen = {s}
for m in range(2, 1000001):
    s = f(s)
    if s in seen:
        print(m)
        break
    seen.add(s)
