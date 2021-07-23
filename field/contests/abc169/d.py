import collections
import math


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

a = factorization(N)
a = [aa[1] for aa in a if aa[0] != 1]
a = collections.Counter(a)

ans = 0
for k, v in a.items():
    n = int((-1 + math.sqrt(1 + 8 * k)) / 2)
    ans += n * v

print(ans)
