N, M = map(int, input().split())

num = [None] * N
for _ in range(M):
    s, c = map(int, input().split())

    if num[s - 1] is None or num[s - 1] == c:
        num[s - 1] = c
    else:
        print(-1)
        break

    if s == 1 and c == 0 and N != 1:
        print(-1)
        break
else:
    ans = 0
    for i in range(N):
        if num[i] is None:
            if i == 0 and N != 1:
                num[i] = 1
            else:
                num[i] = 0
        ans += 10 ** (N - i - 1) * num[i]
    print(ans)
