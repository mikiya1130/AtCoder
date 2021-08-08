N = input()

n = len(N)
if n % 2 == 0:
    N = "9" * (n - 1)
    n -= 1

N = int(N)

if n == 1:
    print(N)
elif n == 3:
    print(9 + N - 99)
elif n == 5:
    print(9 + 900 + N - 9999)
