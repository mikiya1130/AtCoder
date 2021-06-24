N = int(input())
A = list(map(int, input().split()))

ans = float('inf')

for i in range(1 << N-1):
    tmp_or = A[0]
    tmp_xor = 0

    for j in range(1, N):
        if ((i >> j-1) & 0b1) == 0:
            tmp_or |= A[j]
        else:
            tmp_xor ^= tmp_or
            tmp_or = A[j]

    tmp_xor ^= tmp_or
    ans = min(ans, tmp_xor)

print(ans)
