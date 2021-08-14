a, b = map(int, input().split())
n = b - a
print(sum(range(1, n + 1)) - b)
