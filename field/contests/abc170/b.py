X, Y = map(int, input().split())

b = (Y - 2 * X) / 2

if b.is_integer() and 0 <= int(b) <= X:
    print("Yes")
else:
    print("No")
