N, C = map(int, input().split())

L = {}
for i in range(N):
    a, b, c = map(int, input().split())

    L.setdefault(a, 0)
    L[a] += c

    L.setdefault(b+1, 0)
    L[b+1] -= c

sort_key = sorted(L)

sum = 0
x = 0
for k1, k2 in zip(sort_key[:-1], sort_key[1:]):
    x += L[k1]
    d = k2 - k1
    sum += min(x, C) * d

print(sum)
