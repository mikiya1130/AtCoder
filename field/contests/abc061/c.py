from collections import defaultdict
import itertools
import bisect

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

d = defaultdict(int)
for a, b in AB:
    d[a] += b

l = sorted(d.items())
acc = tuple(itertools.accumulate([v for _, v in l]))

idx = bisect.bisect_left(acc, K)
print(l[idx][0])
