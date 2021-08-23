def factorization(n):
    arr = {}
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt
    if temp != 1:
        arr[temp] = 1

    if arr == []:
        arr[n] = 1

    return arr


N = int(input())
A = list(map(int, input().split()))

ans = 2 ** 30
for a in A:
    arr = factorization(a)
    if 2 in arr:
        ans = min(ans, arr[2])
    else:
        ans = 0
        break

print(ans)
