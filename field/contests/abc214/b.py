import itertools

S, T = map(int, input().split())

ans = 0
for a, b, c in itertools.product(range(S + 1), repeat=3):
    if a + b + c <= S and a * b * c <= T:
        ans += 1

print(ans)
