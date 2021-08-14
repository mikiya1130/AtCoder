N = int(input())

s = 0
n = N
while n > 0:
    s += n % 10
    n //= 10

if N % s == 0:
    print("Yes")
else:
    print("No")
