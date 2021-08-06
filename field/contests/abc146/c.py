A, B, X = map(int, input().split())


def f(a, b, n, d):
    return a * n + b * d


minN = None
maxN = None
d = None

for i in range(10):
    tmpN = 10 ** i
    d = i + 1

    s = f(A, B, tmpN, d)
    if s <= X:
        continue
    else:
        maxN = tmpN - 1
        minN = tmpN // 10
        d -= 1
        break
else:
    minN = maxN = tmpN

print(min(int((X - B * d) // A), maxN))
