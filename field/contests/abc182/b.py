import numpy as np


def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2, N + 1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


N = int(input())
A = list(map(int, input().split()))

prime = seachPrimeNum(1000)

ans = 0
ans_n = 0
for p in prime:
    count = 0
    for a in A:
        if a % p == 0:
            count += 1
    if count > ans_n:
        ans = p
        ans_n = count

print(ans)
