N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True) + [0]
B = [A[i] - A[i + 1] for i in range(N)]

n = 1
ans = 0
while K > 0:
    if n > N:
        break
    if K >= B[n - 1] * n:
        ans += (B[n - 1] * (A[n] + 1 + A[n - 1]) // 2) * n
        K -= B[n - 1] * n
        n += 1
    else:
        div, mod = divmod(K, n)
        ans += (div * (A[n - 1] - div + 1 + A[n - 1]) // 2) * n
        ans += (A[n - 1] - div) * mod
        break

print(ans)
