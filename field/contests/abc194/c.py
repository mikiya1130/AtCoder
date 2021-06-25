import collections
import itertools

N = int(input())
A = list(map(int, input().split()))
A = collections.Counter(A)

sum = 0
for i, j in itertools.combinations(A, 2):
    sum += (i - j)**2 * A[i] * A[j]

print(sum)
