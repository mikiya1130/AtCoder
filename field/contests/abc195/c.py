import math

N = input()

a = len(N)
b = math.ceil(a / 3)

count = 0
for i in range(1, b):
    count += (10**(3*i) - 10**(3*(i-1))) * (i-1)

count += (int(N) - 10**(3*(b-1)) + 1) * (b-1)

print(count)
