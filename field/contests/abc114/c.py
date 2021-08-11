def inc(x):
    for i in range(len(x) - 1, -1, -1):
        if x[i] == 3:
            x[i] = 5
            break
        elif x[i] == 5:
            x[i] = 7
            break
        elif x[i] == 7:
            x[i] = 3
            continue
    else:
        x = [3] + x
    return x


N = int(input())

i = [3, 3, 3]
cnt = 0
while int("".join(map(str, i))) <= N:
    if set(i) == {3, 5, 7}:
        cnt += 1
    i = inc(i)

print(cnt)
