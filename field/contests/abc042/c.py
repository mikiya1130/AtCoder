N, K = map(int, input().split())
D = set(map(int, input().split()))

D = set(range(10)) - D
D = sorted(list(D))

ans = ""
while N > 0:
    i = N % 10
    N //= 10

    for d in D:
        if i == d:
            ans = str(i) + ans
            break
        elif i < d:
            ans = str(d) + str(D[0]) * len(ans)
            break
    else:
        N += 1
        ans = str(D[0]) * (len(ans) + 1)

print(ans)
