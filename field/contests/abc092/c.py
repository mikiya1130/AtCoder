N = int(input())
A = list(map(int, input().split()))

A = [0] + A + [0]
route = 0
skip = []
for i in range(N + 1):
    route += abs(A[i] - A[i + 1])
    skip += [abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i]) - abs(A[i + 1] - A[i - 1])]

for s in skip[1:]:
    print(route - s)
