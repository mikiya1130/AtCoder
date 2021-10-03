S = input()

pre = S[0]
cnt = 1
for s in S[1:]:
    if pre == s:
        cnt += 1
    else:
        print(pre, end="")
        print(cnt, end="")
        cnt = 1
    pre = s
print(pre, end="")
print(cnt)
