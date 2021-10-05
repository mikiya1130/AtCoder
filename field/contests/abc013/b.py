a, b = [int(input()) for _ in range(2)]

if a > b:
    a, b = b, a
c = a + 10
ans = min(b - a, c - b)

print(ans)
