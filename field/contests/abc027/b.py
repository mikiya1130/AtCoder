N = int(input())
A = list(map(int, input().split()))

m = sum(A) // N

if m * N != sum(A):
    print(-1)
else:
    ans = 0
    move = 0
    for a in A:
        move += m - a
        if move != 0:
            ans += 1

    print(ans)
