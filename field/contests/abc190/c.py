N, M = map(int, input().split())

AB = []
for i in range(M):
    AB.append(tuple(map(int, input().split())))

K = int(input())

CD = []
for i in range(K):
    CD.append(tuple(map(int, input().split())))

ans = 0
for i in range(2**K):
    dishes = [False] * N
    for j, cd in enumerate(CD):
        dish = cd[i >> j & 1]
        dishes[dish-1] = True

    count = 0
    for ab in AB:
        if dishes[ab[0]-1] and dishes[ab[1]-1]:
            count += 1

    ans = max(ans, count)

print(ans)
