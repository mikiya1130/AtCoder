N = int(input())
i = N // 4
for x in range(i + 1):
    if (N - 4 * x) % 7 == 0:
        print("Yes")
        break
else:
    print("No")
