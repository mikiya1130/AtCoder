import itertools

N = int(input())
L = []
for _ in range(N):
    L.append(tuple(tuple(map(int, input().split())) for _ in range(int(input()))))

for people in itertools.product((1, 0), repeat=N):
    next = False

    for i, l in enumerate(L):
        if people[i] == 0:
            continue

        for x, y in l:
            if people[x - 1] != y:
                next = True
                break

        if next:
            break

    else:
        print(sum(people))
        break
else:
    print(0)
