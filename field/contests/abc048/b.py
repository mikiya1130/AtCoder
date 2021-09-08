a, b, x = map(int, input().split())

first = (a + x - 1) // x
last = b // x

print(last - first + 1)
