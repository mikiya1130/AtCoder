H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

L = []
for i, a in enumerate(A, 1):
    L += [i] * a

for i in range(H):
    ans = L[W * i : W * (i + 1)]
    if i % 2 == 1:
        ans = reversed(ans)
    print(*ans)
