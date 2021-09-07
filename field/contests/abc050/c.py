import collections

N = int(input())
A = list(map(int, input().split()))

A = collections.Counter(A)
for i in range((N + 1) % 2, N, 2):
    if (i not in A) or (i != 0 and A[i] != 2) or (i == 0 and A[i] != 1):
        print(0)
        break
else:
    print(pow(2, (N // 2), 10 ** 9 + 7))
