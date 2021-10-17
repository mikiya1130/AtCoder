X = int(input())
div, mod = divmod(X, 100)
if div >= 1 and mod == 0:
    print("Yes")
else:
    print("No")
