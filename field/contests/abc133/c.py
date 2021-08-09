import itertools

L, R = map(int, input().split())

if R - L > 2019:
    R = L + 2019

ans = 2019
for l, r in itertools.combinations(range(L, R + 1), 2):
    ans = min(ans, (l * r) % 2019)
    if ans == 0:
        break

print(ans)
