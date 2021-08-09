N, M = map(int, input().split())
K = []
for _ in range(M):
    S = list(map(int, input().split()))
    K.append([s - 1 for s in S[1:]])
P = list(map(int, input().split()))

ans = 0
for i in range(2 ** N):
    nSW = [0] * M

    for m, s in enumerate(K):
        for n in s:
            if (i >> n) & 1:
                nSW[m] ^= 1

    for n, p in zip(nSW, P):
        if n != p:
            break
    else:
        ans += 1

print(ans)
