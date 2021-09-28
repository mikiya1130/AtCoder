K = int(input())
A, B = map(int, input().split())

A_10 = 0
B_10 = 0

i = 0
while A > 0:
    A, mod = divmod(A, 10)
    A_10 += mod * K ** i
    i += 1

i = 0
while B > 0:
    B, mod = divmod(B, 10)
    B_10 += mod * K ** i
    i += 1

print(A_10 * B_10)
