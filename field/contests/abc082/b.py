s = list(input())
t = list(input())

s = "".join(sorted(s))
t = "".join(sorted(t, reverse=True))

l = min(len(s), len(t))

for ss, tt in zip(s[:l], t[:l]):
    if ss < tt:
        print("Yes")
        break
    elif ss > tt:
        print("No")
        break
else:
    if len(s) < len(t):
        print("Yes")
    else:
        print("No")
