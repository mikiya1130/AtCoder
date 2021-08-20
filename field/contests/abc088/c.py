C = [list(map(int, input().split())) for _ in range(3)]

for a1 in range(C[0][0] + 1):
    b1 = C[0][0] - a1

    b2 = C[0][1] - a1
    b3 = C[0][2] - a1

    a2 = C[1][0] - b1
    a3 = C[2][0] - b1

    if b2 < 0 or b3 < 0 or a2 < 0 or a3 < 0:
        continue

    if (
        a2 + b2 != C[1][1]
        or a2 + b3 != C[1][2]
        or a3 + b2 != C[2][1]
        or a3 + b3 != C[2][2]
    ):
        continue

    print("Yes")
    break
else:
    print("No")
