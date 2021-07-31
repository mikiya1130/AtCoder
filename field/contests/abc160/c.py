K, N = map(int, input().split())
A = list(map(int, input().split()))

_max = 0
for i in range(N - 1):
    diff = A[i + 1] - A[i]
    _max = max(_max, diff)

diff = K - A[-1] + A[0]
_max = max(_max, diff)

print(K - _max)
