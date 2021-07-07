N = list(input())

mod = [0] * 3

for n in N:
    mod[int(n) % 3] += 1

a = (1 * mod[1] + 2 * mod[2]) % 3

l = len(N)

if a % 3 == 0:
    print(0)
elif a % 3 == 1:
    if mod[1] != 0:
        if l != 1:
            print(1)
        else:
            print(-1)
    else:
        if l != 2:
            print(2)
        else:
            print(-1)
else:
    if mod[2] != 0:
        if l != 1:
            print(1)
        else:
            print(-1)
    else:
        if l != 2:
            print(2)
        else:
            print(-1)
