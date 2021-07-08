import itertools

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

for p1, p2, p3 in itertools.combinations(P, 3):
    if p1[0] != p2[0]:
        a1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    else:
        a1 = "inf"

    if p1[0] != p3[0]:
        a2 = (p3[1] - p1[1]) / (p3[0] - p1[0])
    else:
        a2 = "inf"

    if a1 == a2:
        print("Yes")
        break
else:
    print("No")
