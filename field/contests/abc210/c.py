import collections

N, K = map(int, input().split())
C = list(map(int, input().split()))

li = collections.Counter(C[:K])
ans = len(li)
for i in range(N - K):
    li[C[i]] -= 1
    if li[C[i]] == 0:
        li.pop(C[i])

    if C[i + K] in li:
        li[C[i + K]] += 1
    else:
        li[C[i + K]] = 1

    ans = max(ans, len(li))

print(ans)
