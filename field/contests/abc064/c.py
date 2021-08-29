N = int(input())
A = list(map(int, input().split()))

color = [False] * 8
over = 0
for a in A:
    if a >= 3200:
        over += 1
    else:
        color[a // 400] = True

print(max(sum(color), 1), sum(color) + over)
