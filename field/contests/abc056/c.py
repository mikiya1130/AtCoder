import itertools
import bisect

X = int(input())

N = tuple(itertools.accumulate(range(1, 10 ** 5)))
print(bisect.bisect_left(N, X) + 1)
