N = int(input())
S = input()

if N % 2 != 1:
    print(-1)
else:

    def f(s, i):
        i += 1
        if i % 3 == 1:
            s = "a" + s + "c"
        elif i % 3 == 2:
            s = "c" + s + "a"
        else:
            s = "b" + s + "b"
        return s

    s = "b"
    if s == S:
        print(0)
    else:
        for i in range(N // 2):
            s = f(s, i)

        if s == S:
            print(i + 1)
        else:
            print(-1)
