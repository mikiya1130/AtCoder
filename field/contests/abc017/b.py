X = input()

next_h = False
for x in X:
    if next_h:
        if x == "h":
            next_h = False
            continue
        else:
            print("NO")
            break
    if x == "c":
        next_h = True
        continue
    elif x in "oku":
        continue
    else:
        print("NO")
        break
else:
    if not next_h:
        print("YES")
    else:
        print("NO")
