import itertools

n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

L = [0] * (1000000 + 2)
for a, b in AB:
    L[a] += 1
    L[b + 1] -= 1

L = itertools.accumulate(L)

print(max(L))
