S = input()

idx = 0
while idx < len(S):
    if S[idx : idx + 11] == "dreameraser":
        idx += 11
    elif S[idx : idx + 10] == "dreamerase":
        idx += 10
    elif S[idx : idx + 7] == "dreamer":
        idx += 7
    elif S[idx : idx + 5] == "dream":
        idx += 5
    elif S[idx : idx + 6] == "eraser":
        idx += 6
    elif S[idx : idx + 5] == "erase":
        idx += 5
    else:
        print("NO")
        break
else:
    print("YES")
