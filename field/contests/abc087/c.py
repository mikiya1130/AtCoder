import itertools

N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

A1 = tuple(itertools.accumulate(A1))
A2 = tuple(reversed(tuple(itertools.accumulate(reversed(A2)))))

ans = 0
for a1, a2 in zip(A1, A2):
    ans = max(ans, a1 + a2)

print(ans)
