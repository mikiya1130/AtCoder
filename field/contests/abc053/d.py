import collections

N = int(input())
A = list(map(int, input().split()))

A = collections.Counter(A)

sum_ = 0
for a in A.values():
    sum_ += a - 1
sum_ += sum_ % 2

print(N - sum_)
