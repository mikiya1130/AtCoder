s = input()

ans = ""
cnt = 0
for ss in reversed(s):
    if ss == "B":
        cnt += 1
    else:
        if cnt == 0:
            ans = ss + ans
        else:
            cnt -= 1

print(ans)
