def factorization(n):
    arr = set()
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            arr.add(i)
    if temp != 1:
        arr.add(temp)

    if arr == []:
        arr.add(n)

    return arr


N, M = map(int, input().split())
A = list(map(int, input().split()))

S = set()
for a in A:
    S |= factorization(a)

T = set(range(1, M + 1))
for s in S:
    U = set(range(s, M + 1, s))
    T -= U

print(len(T))
for t in T:
    print(t)
