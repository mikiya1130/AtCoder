import math

N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

comfort = A[0]
half = math.ceil(N / 2)
for a in A[1:half]:
    comfort += a * 2

if N % 2 == 1:
    comfort -= A[half - 1]

print(comfort)
