S = input()
T = input()

for s, t in zip(S, T):
    if s == t:
        continue
    elif s == "@" and t in "atcoder":
        continue
    elif t == "@" and s in "atcoder":
        continue
    else:
        print("You will lose")
        break
else:
    print("You can win")
