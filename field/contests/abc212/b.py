X = input()
X1, X2, X3, X4 = [int(x) for x in X]

if X1 == X2 == X3 == X4:
    print("Weak")
else:
    if (
        (X2 + 10 - X1) % 10 == 1
        and (X3 + 10 - X2) % 10 == 1
        and (X4 + 10 - X3) % 10 == 1
    ):
        print("Weak")
    else:
        print("Strong")
