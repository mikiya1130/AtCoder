import math

N = int(input())
for k in range(70):
    if 2 ** k > N:
        print(k - 1)
        break
