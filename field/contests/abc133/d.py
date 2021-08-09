N = int(input())
A = list(map(int, input().split()))

M = [0] * N
M[0] = A[0]
for i in range(1, N, 2):
    M[0] += -A[i] + A[i + 1]

for i in range(1, N):
    M[i] = 2 * (A[i - 1] - M[i - 1] // 2)

print(*M)
