import itertools

N = int(input())
A = list(map(int, input().split()))

L = tuple(itertools.accumulate(A))
R = tuple(reversed(tuple(itertools.accumulate(reversed(A)))))

ans = 10 ** 10
for l, r in zip(L[:-1], R[1:]):
    ans = min(ans, abs(l - r))

print(ans)
