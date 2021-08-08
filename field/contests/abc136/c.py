N = int(input())
H = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    diff = H[i - 1] - H[i]

    if diff > 1:
        print("No")
        break

    if diff == 1:
        H[i - 1] -= 1
else:
    print("Yes")
