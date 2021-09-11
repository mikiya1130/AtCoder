A = input()
B = input()
C = input()


def f(s):
    return s[1:], s[0]


next = "a"
while True:
    if next == "a":
        if len(A) == 0:
            print("A")
            break
        A, next = f(A)
    if next == "b":
        if len(B) == 0:
            print("B")
            break
        B, next = f(B)
    if next == "c":
        if len(C) == 0:
            print("C")
            break
        C, next = f(C)
