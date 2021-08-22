def ceil(a, b):
    return (a + b - 1) // b


a, b = map(int, input().split())

print(ceil(a + b, 2))
