N = int(input())

arr = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        print(i)
        if N // i != i:
            arr.append(N // i)

for i in reversed(arr):
    print(i)
