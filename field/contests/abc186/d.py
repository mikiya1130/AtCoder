import itertools

N = int(input())
A = list(map(int, input().split()))

A.sort()

S = list(itertools.accumulate(A))

sum = 0
for i, li in enumerate(zip(A[1:], S[:-1]), 1):
    a, s = li[0], li[1]
    sum += i * a - s

print(sum)
