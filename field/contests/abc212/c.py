N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

i, j = 0, 0
ans = 10 ** 9
while i < N and j < M:
    ans = min(ans, abs(A[i] - B[j]))

    if A[i] < B[j]:
        i += 1
        if i >= N:
            i -= 1
            j += 1
    else:
        j += 1
        if j >= M:
            j -= 1
            i += 1

print(ans)
