N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0]
next = 0
seen = [False] * N
seen[0] = True
for i in range(N):
    b = A[next] - 1
    if seen[b] == False:
        B.append(b)
        next = b
        seen[b] = True
        continue
    else:
        idx = B.index(b)
        loop = i - idx + 1
        break

if idx > K:
    print(B[K] + 1)
else:
    K -= idx
    K %= loop
    print(B[idx + K] + 1)
