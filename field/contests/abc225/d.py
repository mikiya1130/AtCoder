N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

prev = [None] * N
next = [None] * N

for n, *l in Query:
    if n != 3:
        x, y = l
        x -= 1
        y -= 1
    else:
        x = l[0] - 1

    if n == 1:
        next[x] = y
        prev[y] = x
    elif n == 2:
        next[x] = None
        prev[y] = None
    elif n == 3:
        i = x
        while prev[i] is not None:
            i = prev[i]

        l = [i + 1]
        while next[i] is not None:
            i = next[i]
            l.append(i + 1)

        print(len(l), *l)
