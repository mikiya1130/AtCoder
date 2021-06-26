import itertools

N = int(input())

list = []
for i in range(N):
    t, l, r = map(int, input().split())

    if t == 1:
        pass
    elif t == 2:
        r -= 0.5
    elif t == 3:
        l += 0.5
    elif t == 4:
        l += 0.5
        r -= 0.5

    list.append((l, r))

count = 0
for i, j in itertools.combinations(list, 2):
    if (i[0] <= j[1] and j[0] <= i[1]):
        count += 1

print(count)
