P = int(input())

factorial = (3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1)

ans = 0
for f in factorial:
    ans += P // f
    P %= f

print(ans)
