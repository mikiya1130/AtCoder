import math

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]

for x, y in XY:
    if (
        math.sqrt((txa - x) ** 2 + (tya - y) ** 2)
        + math.sqrt((txb - x) ** 2 + (tyb - y) ** 2)
        <= T * V
    ):
        print("YES")
        break
else:
    print("NO")
