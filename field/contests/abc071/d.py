N = int(input())
S1 = input()
S2 = input()


def update(pattern, dir):
    global ans, i, pre

    ans *= pattern
    ans %= 1000000007
    pre = dir
    if dir == "h":
        i += 2
    else:
        i += 1


if N == 1:
    print(3)
    exit()

if S1[0] == S1[1]:
    ans = 6
    pre = "h"
    i = 2
else:
    ans = 3
    pre = "v"
    i = 1

while i < N - 1:
    if pre == "h":
        if S1[i] == S1[i + 1]:
            update(3, "h")
        else:
            update(1, "v")
    else:
        if S1[i] == S1[i + 1]:
            update(2, "h")
        else:
            update(2, "v")

if i == N - 1:
    if pre == "v":
        update(2, "v")

print(ans)
