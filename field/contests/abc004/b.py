C = [input() for _ in range(4)]

ans = []
for row in reversed(C):
    tmp = ""
    for c in reversed(row):
        tmp += c
    ans += [tmp]

print(*ans, sep="\n")
