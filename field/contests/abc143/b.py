import itertools

N = int(input())
D = list(map(int, input().split()))

ans = 0
for x, y in itertools.combinations(D, 2):
    ans += x * y

print(ans)
