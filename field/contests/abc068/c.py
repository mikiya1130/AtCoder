N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

start = set()
goal = set()
for a, b in AB:
    if a == 1:
        start.add(b)
    elif b == 1:
        start.add(a)
    if a == N:
        goal.add(b)
    elif b == N:
        goal.add(a)

if start & goal:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
