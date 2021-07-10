N = int(input())
C = list(map(int, input().split()))

C.sort()

prod = 1
a = 10 ** 9 + 7
for i in range(N):
    prod *= C[i] - i
    prod %= a

print(prod)
