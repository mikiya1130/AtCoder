import itertools
import bisect

N, X = map(int, input().split())
L = list(map(int, input().split()))

L = list(itertools.accumulate([0] + L))
print(bisect.bisect_right(L, X))
