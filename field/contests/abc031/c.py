N = int(input())
A = list(map(int, input().split()))

ans = -1300
for t in range(N):
    tmp_t = None
    tmp_a = -1300
    for a in range(N):
        if t == a:
            continue

        if t < a:
            T = A[t : a + 1]
        else:
            T = A[a : t + 1]

        sum_a = sum(T[1::2])
        if sum_a > tmp_a:
            tmp_t = sum(T[0::2])
            tmp_a = sum_a

    ans = max(ans, tmp_t)

print(ans)
