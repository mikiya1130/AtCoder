A, B = map(int, input().split())

for n in range(20):
    if (A - 1) * n + 1 >= B:
        print(n)
        break
