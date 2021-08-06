N = int(input())
S = input()

ans = ""
for s in S:
    ch = ord(s) - ord("A")
    ch = (ch + N) % 26
    ch = ch + ord("A")
    ans += chr(ch)

print(ans)
