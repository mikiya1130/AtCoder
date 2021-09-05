from collections import defaultdict


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N = int(input())

F = defaultdict(int)
for i in range(2, N + 1):
    fact = factorization(i)
    for k, v in fact:
        F[k] += v

ans = 1
MOD = 1000000007
for _, v in F.items():
    ans = ans * (v + 1) % MOD

print(ans)
