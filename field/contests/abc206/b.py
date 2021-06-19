N = int(input())

for i in range(10**8):
    N -= i
    if N <= 0:
        break

print(i)
