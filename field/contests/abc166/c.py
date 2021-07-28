N, M = map(int, input().split())
H = list(map(int, input().split()))

L = [set() for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    L[A - 1].add(H[B - 1])
    L[B - 1].add(H[A - 1])

ans = 0
for i, l in enumerate(L):
    if not l or max(l) < H[i]:
        ans += 1

print(ans)
