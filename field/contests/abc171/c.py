N = int(input())

alphabet = [chr(a) for a in range(97, 123)]

ans = ""
while N != 0:
    N -= 1
    ans = alphabet[N % 26] + ans
    N //= 26

print(ans)
