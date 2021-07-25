li = [False] * 4

for _ in range(4):
    S = input()

    if S == "H":
        li[0] = True
    elif S == "2B":
        li[1] = True
    elif S == "3B":
        li[2] = True
    elif S == "HR":
        li[3] = True

if all(li):
    print("Yes")
else:
    print("No")
