N = int(input())

for i in range(1, 10):
    div, mod = divmod(N, i)

    if 1 <= div <= 9 and mod == 0:
        print("Yes")
        break
else:
    print("No")
