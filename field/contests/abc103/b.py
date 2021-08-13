S = input()
T = input()

l = len(T)
for i in range(l):
    for s, t in zip(S, T[i:] + T[:i]):
        if s != t:
            break
    else:
        print("Yes")
        break
else:
    print("No")
