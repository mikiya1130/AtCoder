N = int(input())
SP = [input().split() for _ in range(N)]

_max = 0
_max_name = None
_sum = 0

for s, p in SP:
    p = int(p)
    _sum += p
    if _max < p:
        _max = p
        _max_name = s

if _sum / 2 < _max:
    print(_max_name)
else:
    print("atcoder")
