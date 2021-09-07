import itertools

K, S = map(int, input().split())

ans = 0
for x, y in itertools.product(range(K + 1), repeat=2):
    if 0 <= S - (x + y) <= K:
        ans += 1

print(ans)
