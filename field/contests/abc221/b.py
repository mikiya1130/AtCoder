S = input()
T = input()

change = "before"
for i, (s, t) in enumerate(zip(S, T)):
    if s != t:
        if change == "before":
            if not (i < len(S) - 1 and S[i] == T[i + 1] and T[i] == S[i + 1]):
                print("No")
                break
            change = "progress"
        elif change == "progress":
            change = "done"
            continue
        elif change == "done":
            print("No")
            break
else:
    print("Yes")
