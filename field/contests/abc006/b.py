n = int(input())

MOD = 10007

T = [0] * (n - 1)
T[0:3] = [0, 0, 1, 1]
S = sum(T[1:3])
for i in range(4, n):
    T[i] = S + T[i - 1] - T[i - 4]
    T[i] %= MOD
    S = T[i]

print(T[n - 1])
