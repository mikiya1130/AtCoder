N = int(input())

for x in range(N, N + 111):
    if len(set(str(x))) == 1:
        print(x)
        break
