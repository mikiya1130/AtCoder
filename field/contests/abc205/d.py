import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

count = [0] * N
count[0] = A[0] - 1
for i in range(1, N):
    count[i] = count[i-1] + (A[i] - A[i-1] - 1)

for i in range(Q):
    K = int(input())
    index = bisect.bisect_left(count, K)
    print(K + index)
