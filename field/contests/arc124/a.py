N, K = map(int, input().split())

card = [[] for _ in range(N)]
write = [False] * N

for _ in range(K):
    c, k = input().split()
    k = int(k)

    card[k - 1] = [k - 1]
    write[k - 1] = True

    if c == "L":
        for kk in range(k, N):
            if not write[kk]:
                card[kk].append(k - 1)
    elif c == "R":
        for kk in range(k - 1):
            if not write[kk]:
                card[kk].append(k - 1)

ans = 1
for c in card:
    ans *= len(c)

print(ans % 998244353)
