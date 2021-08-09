N = int(input())
A = list(map(int, input().split()))
A = ["dummy"] + A

M = 0
B = []
C = ["dummy"] + [0] * N

for i in range(N, 0, -1):
    cnt = 0

    for j in range(i * 2, N + 1, i):
        cnt += C[j]

    C[i] = A[i] ^ (cnt % 2)
    if C[i] == 1:
        M += 1
        B.append(i)

print(M)
if M:
    print(*B)
