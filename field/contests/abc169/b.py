N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
else:
    limit = 10 ** 18
    ans = 1
    for a in A:
        ans *= a
        if ans > limit:
            print(-1)
            break
    else:
        print(ans)
