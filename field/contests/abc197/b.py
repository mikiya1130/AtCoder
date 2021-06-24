H, W, X, Y = map(int, input().split())

row = ''
col = ''
for h in range(H):
    str = input()

    col += str[Y-1]

    if h == X-1:
        row += str


def countDot(list, idx):
    count = 0

    for str in list[idx:]:
        if str == '#':
            break
        count += 1

    for str in reversed(list[:idx]):
        if str == '#':
            break
        count += 1

    return count


sum = countDot(col, X-1) + countDot(row, Y-1) - 1
print(sum)
