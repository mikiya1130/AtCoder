N = int(input())

ans = N
i = 1
while i * i <= N:
    if N % i == 0:
        ans = min(ans, (i - 1) + (N // i - 1))
    i += 1

print(ans)
