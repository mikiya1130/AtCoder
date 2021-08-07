N = int(input())
S = input()

ans = 0
pre = None
for s in S:
    if s != pre:
        ans += 1
        pre = s

print(ans)
